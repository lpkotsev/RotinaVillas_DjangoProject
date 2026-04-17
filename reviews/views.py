from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Review
from .forms import ReviewForm
from villas.models import Villa
from django.shortcuts import redirect

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_create.html"

    def dispatch(self, request, *args, **kwargs):
        self.villa = get_object_or_404(Villa, pk=kwargs["pk"])
        if Review.objects.filter(villa=self.villa, user=request.user).exists():
            return redirect("villa-details", pk=self.villa.pk)

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        review = form.save(commit=False)
        review.user = self.request.user
        review.villa = self.villa
        review.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("villa-details", kwargs={"pk": self.villa.pk})