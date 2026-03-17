from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Villa
from .forms import VillaCreateForm, VillaEditForm


class VillaListView(ListView):

    model = Villa

    template_name = "villas/villa-list.html"

    context_object_name = "villas"


class VillaDetailView(DetailView):

    model = Villa

    template_name = "villas/villa-details.html"


class VillaCreateView(CreateView):

    model = Villa

    form_class = VillaCreateForm

    template_name = "villas/villa-create.html"

    success_url = reverse_lazy("villa-list")


class VillaEditView(UpdateView):

    model = Villa

    form_class = VillaEditForm

    template_name = "villas/villa-edit.html"

    success_url = reverse_lazy("villa-list")


class VillaDeleteView(DeleteView):

    model = Villa
    template_name = "villas/villa-delete.html"
    success_url = reverse_lazy("villa-list")

class MyVillasView(ListView):
    model = Villa
    template_name = "villas/my-villas.html"
    context_object_name = "villas"

# Create your views here.
