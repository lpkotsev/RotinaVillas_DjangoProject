from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class BookingAPITest(APITestCase):

    def test_requires_auth(self):
        response = self.client.get("/api/bookings/")
        self.assertEqual(response.status_code, 403)

    def test_authenticated_access(self):
        user = User.objects.create_user(username="user", password="123")
        self.client.login(username="user", password="123")

        response = self.client.get("/api/bookings/")
        self.assertEqual(response.status_code, 200)

    def test_api_requires_auth(self):
        response = self.client.get("/api/bookings/")
        self.assertEqual(response.status_code, 403)

    def test_villas_api_public(self):
        response = self.client.get("/api/villas/")
        self.assertEqual(response.status_code, 200)

    def test_api_returns_json(self):
        response = self.client.get("/api/villas/")
        self.assertEqual(response["Content-Type"], "application/json")
