from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Review
from .forms import ReviewForm
from villas.models import Villa
from django.shortcuts import redirect
from bookings.models import Booking
from villas.models import Villa
from datetime import date

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_create.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.guest_name = self.request.user.username
        self.object.user = self.request.user
        self.object.villa = self.villa
        self.object.save()
        return redirect("villa-details-page", pk=self.villa.pk)

    def dispatch(self, request, *args, **kwargs):
        self.villa = get_object_or_404(Villa, pk=self.kwargs["pk"])


        has_booking = Booking.objects.filter(
            user=request.user,
            villa=self.villa,
            check_out__lt=date.today()
        ).exists()

        if not has_booking:
            return redirect("villa-details-page", pk=self.villa.pk)


        if Review.objects.filter(
            user=request.user,
            villa=self.villa
        ).exists():
            return redirect("villa-details-page", pk=self.villa.pk)

        return super().dispatch(request, *args, **kwargs)