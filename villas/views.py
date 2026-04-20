from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from common.mixins import IsOwnerOrModeratorMixin
from .models import Villa
from .forms import VillaCreateForm, VillaEditForm, VillaSearchForm, VillaFilterForm




class VillaListView(ListView):

    model = Villa

    template_name = "villas/villa-list.html"

    context_object_name = "villas"

    def get_queryset(self):
        queryset = super().get_queryset()

        self.search_form = VillaSearchForm(self.request.GET)
        self.filter_form = VillaFilterForm(self.request.GET)


        if self.search_form.is_valid():
            query = self.search_form.cleaned_data.get("query")

            if query:
                queryset = queryset.filter(
                    Q(name__icontains=query) |
                    Q(location__icontains=query)
                )


        if self.filter_form.is_valid():

            min_price = self.filter_form.cleaned_data.get("min_price")
            max_price = self.filter_form.cleaned_data.get("max_price")
            guests = self.filter_form.cleaned_data.get("guests")
            ordering = self.filter_form.cleaned_data.get("ordering")


            if min_price:
                queryset = queryset.filter(price_per_night__gte=min_price)

            if max_price:
                queryset = queryset.filter(price_per_night__lte=max_price)


            if guests:
                queryset = queryset.filter(capacity__gte=guests)

            check_in = self.filter_form.cleaned_data.get("check_in")
            check_out = self.filter_form.cleaned_data.get("check_out")

            if check_in and check_out:
                queryset = queryset.exclude(
                    bookings__check_in__lt=check_out,
                    bookings__check_out__gt=check_in
                )


            if ordering:
                queryset = queryset.order_by(ordering)

        return queryset


    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["search_form"] = self.search_form
       context["filter_form"] = self.filter_form
       return context

class VillaDetailView(DetailView):

    model = Villa

    template_name = "villas/villa-details.html"


class VillaCreateView(LoginRequiredMixin, CreateView):
     model = Villa
     form_class = VillaCreateForm
     template_name = 'villas/villa-create.html'
     success_url = reverse_lazy('villa-list-page')

     def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)




class VillaEditView(LoginRequiredMixin, IsOwnerOrModeratorMixin, UpdateView):

    model = Villa

    form_class = VillaEditForm

    template_name = "villas/villa-edit.html"

    success_url = reverse_lazy("villa-list-page")




class VillaDeleteView(LoginRequiredMixin, IsOwnerOrModeratorMixin, DeleteView):

    model = Villa
    template_name = "villas/villa-delete.html"
    success_url = reverse_lazy("villa-list-page")



class MyVillasView(ListView, LoginRequiredMixin):
    model = Villa
    template_name = "villas/my-villas.html"
    context_object_name = "villas"

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser or user.groups.filter(name="Moderators").exists():
            return Villa.objects.all()

        return Villa.objects.filter(owner=user)



# Create your views here.
