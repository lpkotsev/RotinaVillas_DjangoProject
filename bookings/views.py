from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from villas.models import Villa
from .forms import BookingForm
from .models import Booking
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy


def create_booking(request, pk):
    villa = get_object_or_404(Villa, id=pk)

    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():

            check_in = form.cleaned_data["check_in"]
            check_out = form.cleaned_data["check_out"]

            existing_bookings = Booking.objects.filter(
                villa=villa,
                check_in__lt=check_out,
                check_out__gt=check_in
            )

            if existing_bookings.exists():
                messages.error(request, "Unfortunately, this villa is already booked for those dates.")
            else:
                booking = form.save(commit=False)
                booking.villa = villa
                booking.save()

                messages.success(request, "Your booking has been confirmed!")
                return redirect("villa-list")

    else:
        form = BookingForm()

    return render(request, "bookings/booking-create.html", {
        "form": form,
        "villa": villa
    })



class BookingListView(ListView):
    model = Booking
    template_name = "bookings/booking-list.html"
    context_object_name = "bookings"


class BookingEditView(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = "bookings/booking-edit.html"
    success_url = reverse_lazy("my-bookings")


class BookingDeleteView(DeleteView):
    model = Booking
    template_name = "bookings/booking-delete.html"
    success_url = reverse_lazy("my-bookings")