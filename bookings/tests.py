from django.test import TestCase
from django.contrib.auth import get_user_model
from villas.models import Villa
from .models import Booking
from django.urls import reverse
from datetime import date
from bookings.forms import BookingForm


User = get_user_model()

class BookingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="12345"
        )

        self.villa = Villa.objects.create(
            name="Test Villa",
            location="Test Location",
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

    def test_invalid_guests(self):
        form = BookingForm(data={
            "check_in": "2025-01-01",
            "check_out": "2025-01-05",
            "guests": 0,
        })
        self.assertFalse(form.is_valid())

    def test_invalid_dates(self):
        form = BookingForm(data={
            "check_in": "2025-01-05",
            "check_out": "2025-01-01",
            "guests": 2,
        })
        self.assertFalse(form.is_valid())

    def test_overlapping_booking_not_allowed(self):
        Booking.objects.create(
            villa=self.villa,
            user=self.user,
            check_in=date(2025, 1, 1),
            check_out=date(2025, 1, 5),
            guests=2
        )

        form = BookingForm(data={
            "check_in": "2025-01-03",
            "check_out": "2025-01-06",
            "guests": 2,
        })

        self.assertFalse(form.is_valid())

    def test_user_cannot_edit_other_booking(self):
        other_user = User.objects.create_user(username="other")

        booking = Booking.objects.create(
            villa=self.villa,
            user=other_user,
            check_in=date(2025, 1, 1),
            check_out=date(2025, 1, 5),
            guests=2,
        )

        self.client.login(username="test", password="pass")

        response = self.client.get(f"/bookings/{booking.id}/edit/")

        self.assertIn(response.status_code, [302, 403])

    def test_booking_create_requires_login(self):
        response = self.client.get(f"/bookings/create/{self.villa.id}/")
        self.assertEqual(response.status_code, 302)

    def test_booking_create_success(self):
        self.client.login(username="test", password="pass")

        response = self.client.post(f"/bookings/create/{self.villa.id}/", {
            "check_in": "2025-01-01",
            "check_out": "2025-01-05",
            "guests": 2,
        })

        self.assertEqual(response.status_code, 302)


