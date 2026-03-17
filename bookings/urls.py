from django.urls import path
from .views import *

urlpatterns = [
    path("create/<int:pk>/", create_booking, name="booking-create"),
    path("", BookingListView.as_view(), name="my-bookings"),
    path("<int:pk>/edit/", BookingEditView.as_view(), name="booking-edit"),
    path("<int:pk>/delete/", BookingDeleteView.as_view(), name="booking-delete"),
]