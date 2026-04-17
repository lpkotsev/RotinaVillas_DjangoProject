from django.urls import path
from .views import VillaListCreateAPI, BookingListAPI

urlpatterns = [
    path("villas/", VillaListCreateAPI.as_view(), name="api-villas"),
    path("bookings/", BookingListAPI.as_view(), name="api-bookings"),
]
