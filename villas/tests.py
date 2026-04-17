from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Villa
from django.urls import reverse

User = get_user_model()

class VillaModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="12345"
        )

    def test_create_villa(self):
        self.villa = Villa.objects.create(
            name="Test Villa",
            location="Sofia",
            price_per_night=100,
            capacity=4,
            owner=self.user
        )
        self.assertEqual(self.villa.name, "Test Villa")

    def test_villa_str(self):
        self.villa = Villa.objects.create(
            name="Villa",
            location="Sofia",
            price_per_night=100,
            capacity=4,
            owner=self.user
        )
        self.assertEqual(str(self.villa), "Villa - Sofia")



class VillaViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="user", password="123")
        self.client.login(username="user", password="123")
        self.villa = Villa.objects.create(
            name="Test Villa",
            location="Sofia",
            price_per_night=100,
            capacity=4,
            owner=self.user
        )

    def test_villa_list_view(self):
        response = self.client.get(reverse("villa-list"))
        self.assertEqual(response.status_code, 200)

    def test_villa_create_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse("villa-create"))
        self.assertEqual(response.status_code, 302)

    def test_villa_create_logged_in(self):
        self.client.login(username="user", password="123")
        response = self.client.get(reverse("villa-create"))
        self.assertEqual(response.status_code, 200)

    def test_villa_list_empty(self):
        Villa.objects.all().delete()
        response = self.client.get(reverse("villa-list"))
        self.assertEqual(response.status_code, 200)

    def test_villa_detail_view(self):
        response = self.client.get(reverse("villa-details", args=[self.villa.id]))
        self.assertEqual(response.status_code, 200)
