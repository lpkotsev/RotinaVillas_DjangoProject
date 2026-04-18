from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Villa
from .forms import VillaCreateForm, VillaEditForm
from django.views import View
from django.shortcuts import render, redirect
from .forms import VillaCreateForm
from common.mixins import IsObjectOwnerMixin

class VillaListView(ListView):

    model = Villa

    template_name = "villas/villa-list.html"

    context_object_name = "villas"


class VillaDetailView(DetailView):

    model = Villa

    template_name = "villas/villa-details.html"


class VillaCreateView(LoginRequiredMixin, CreateView):
     model = Villa
     form_class = VillaCreateForm
     template_name = 'villas/villa-create.html'
     success_url = reverse_lazy('villa-list')

     def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)




class VillaEditView(LoginRequiredMixin, IsObjectOwnerMixin, UpdateView):

    model = Villa

    form_class = VillaEditForm

    template_name = "villas/villa-edit.html"

    success_url = reverse_lazy("villa-list")


class VillaDeleteView(LoginRequiredMixin, IsObjectOwnerMixin, DeleteView):

    model = Villa
    template_name = "villas/villa-delete.html"
    success_url = reverse_lazy("villa-list")

class MyVillasView(ListView):
    model = Villa
    template_name = "villas/my-villas.html"
    context_object_name = "villas"

    def get_queryset(self):
        return Villa.objects.filter(owner=self.request.user)

# Create your views here.
