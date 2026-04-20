from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path("create/<int:pk>/", BookingCreateView.as_view(), name="booking-create"),
    path("", BookingListView.as_view(), name="my-bookings"),
    path("<int:pk>/edit/", BookingEditView.as_view(), name="booking-edit"),
    path("<int:pk>/delete/", BookingDeleteView.as_view(), name="booking-delete"),
    path("success/", TemplateView.as_view(template_name="bookings/booking-success.html"
), name="booking-success"),
]