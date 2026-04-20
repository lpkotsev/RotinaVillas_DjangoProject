from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrModerator

from villas.models import Villa
from bookings.models import Booking

from .serializers import VillaSerializer, BookingSerializer
from .permissions import IsOwnerOrModerator


class VillaViewSet(viewsets.ModelViewSet):
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["location", "villa_type", "price_per_night"]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrModerator()]
        return [IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser or user.groups.filter(name="Moderators").exists():
            return Booking.objects.all()

        return Booking.objects.filter(user=user)

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrModerator()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
