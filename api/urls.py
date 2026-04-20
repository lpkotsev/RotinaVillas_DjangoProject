from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import VillaViewSet, BookingViewSet

router = DefaultRouter()
router.register("villas", VillaViewSet, basename="villa")
router.register("bookings", BookingViewSet, basename="booking")

urlpatterns = router.urls

