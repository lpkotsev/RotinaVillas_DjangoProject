from django.shortcuts import render, redirect, get_object_or_404

from villas.models import Villa
from .forms import ReviewForm


def create_review(request, pk):

    villa = get_object_or_404(Villa, pk=pk)

    if request.method == "POST":

        form = ReviewForm(request.POST)

        if form.is_valid():

            review = form.save(commit=False)

            review.villa = villa

            review.save()

            return redirect("villa-details", pk=villa.pk)

    else:
        form = ReviewForm()

    context = {
        "form": form,
        "villa": villa,
    }

    return render(request, "reviews/review_create.html", context)

# Create your views here.
