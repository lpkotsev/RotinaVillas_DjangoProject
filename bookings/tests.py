from django.test import TestCase
from django.contrib.auth import get_user_model
from villas.models import Villa
from .models import Booking
from django.urls import reverse

User = get_user_model()

class BookingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="user", password="123")
        self.villa = Villa.objects.create(
            name="Test Villa",
            location="Sofia",
            price_per_night=100,
            capacity=4,
            owner=self.user
        )

    def test_create_booking(self):
        self.booking = Booking.objects.create(
            villa=self.villa,
            user=self.user,
            check_in="2025-01-01",
            check_out="2025-01-05",
            guests=2
        )
        self.assertEqual(self.booking.villa, self.villa)

    def test_booking_str(self):
        booking = Booking.objects.create(
            villa=self.villa,
            user=self.user,
            check_in="2025-01-01",
            check_out="2025-01-05",
            guests=2
        )
        self.assertIn("Test Villa", str(booking))

    def test_booking_create_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse("booking-create", args=[self.villa.id]))
        self.assertEqual(response.status_code, 302)

    def test_booking_create_logged_in(self):
        self.client.login(username="user", password="123")
        response = self.client.get(reverse("booking-create", args=[self.villa.id]))
        self.assertEqual(response.status_code, 200)
