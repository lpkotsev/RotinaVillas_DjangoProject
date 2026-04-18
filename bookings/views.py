from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from villas.models import Villa
from .forms import BookingForm
from .models import Booking
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .tasks import send_booking_confirmation_async
from django.contrib.auth import login
from reviews.models import Review
from datetime import date
from common.mixins import IsObjectOwnerMixin

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking-create.html'

    def dispatch(self, request, *args, **kwargs):
        self.villa = get_object_or_404(Villa, id=self.kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        check_in = form.cleaned_data.get("check_in")
        check_out = form.cleaned_data.get("check_out")


        overlapping_bookings = Booking.objects.filter(
            villa=self.villa,
            check_in__lt=check_out,
            check_out__gt=check_in,
        )

        if overlapping_bookings.exists():
            form.add_error(None, "This villa is already booked for those dates.")
            return self.form_invalid(form)


        booking = form.save(commit=False)
        booking.user = self.request.user
        booking.villa = self.villa
        booking.save()


        send_booking_confirmation_async(booking.id)


        messages.success(self.request, "Booking confirmed!")

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("my-bookings")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["villa"] = self.villa
        return context



class BookingListView(ListView):
    model = Booking
    template_name = "bookings/booking-list.html"

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).select_related("villa")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = date.today()
        context["today"] = today

        bookings_with_flags = []

        for booking in context["object_list"]:
            has_review = Review.objects.filter(
                user=self.request.user,
                villa=booking.villa
            ).exists()

            booking.can_review = booking.check_out < today and not has_review
            bookings_with_flags.append(booking)

        context["bookings"] = bookings_with_flags
        return context


class BookingEditView(LoginRequiredMixin, IsObjectOwnerMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking-edit.html'

    def form_valid(self, form):
        check_in = form.cleaned_data.get("check_in")
        check_out = form.cleaned_data.get("check_out")


        overlapping = Booking.objects.filter(
            villa=self.object.villa,
            check_in__lt=check_out,
            check_out__gt=check_in,
        ).exclude(pk=self.object.pk)

        if overlapping.exists():
            form.add_error(None, "This villa is already booked for those dates.")
            return self.form_invalid(form)

        messages.success(self.request, "Booking updated successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("my-bookings")


class BookingDeleteView(LoginRequiredMixin, IsObjectOwnerMixin, DeleteView):
    model = Booking
    template_name = "bookings/booking-delete.html"
    success_url = reverse_lazy("my-bookings")