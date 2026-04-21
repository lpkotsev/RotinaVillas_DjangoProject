from datetime import date
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from villas.models import Villa
from reviews.models import Review
from common.mixins import IsOwnerOrModeratorMixin
from .models import Booking
from .forms import BookingForm, BookingEditForm
from .tasks import send_booking_confirmation_async


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "bookings/booking-create.html"

    def dispatch(self, request, *args, **kwargs):
        self.villa = get_object_or_404(Villa, id=self.kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        check_in = form.cleaned_data.get("check_in")
        check_out = form.cleaned_data.get("check_out")


        booking = form.save(commit=False)
        booking.user = self.request.user
        booking.villa = self.villa
        booking.save()

        send_booking_confirmation_async.delay(
            self.request.user.email,
            self.villa.name
        )

        messages.success(self.request, "Booking confirmed!")
        return redirect("my-bookings")

    def get_success_url(self):
        return reverse_lazy("booking-success")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["villa"] = self.villa
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["villa"] = self.villa
        return kwargs



class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "bookings/booking-list.html"

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser or user.groups.filter(name="Moderators").exists():
            return Booking.objects.all()

        return Booking.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = date.today()
        user = self.request.user

        context["is_moderator"] = user.groups.filter(name="Moderators").exists()

        bookings_with_flags = []

        for booking in context["object_list"]:
            booking.can_review = booking.check_out < today
            bookings_with_flags.append(booking)

        context["object_list"] = bookings_with_flags

        return context


class BookingEditView(LoginRequiredMixin, IsOwnerOrModeratorMixin, UpdateView):
    model = Booking
    form_class = BookingEditForm
    template_name = "bookings/booking-edit.html"
    success_url = reverse_lazy("my-bookings")



class BookingDeleteView(LoginRequiredMixin, IsOwnerOrModeratorMixin, DeleteView):
    model = Booking
    template_name = "bookings/booking-delete.html"
    success_url = reverse_lazy("my-bookings")
