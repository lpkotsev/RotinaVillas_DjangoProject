from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthTest(TestCase):

    def test_register_user(self):
        response = self.client.post("/accounts/register/", {
            "username": "test",
            "email": "test@test.com",
            "password": "12345test",
            "confirm_password": "12345test",
        })
        self.assertTrue(User.objects.filter(username="test").exists())

    def test_login_user(self):
        User.objects.create_user(username="user", password="123456")
        response = self.client.post(reverse("login"), {
            "username": "user",
            "password": "123456"
        })
        self.assertEqual(response.status_code, 302)

    def test_login_invalid(self):
        User.objects.create_user(username="user", password="123")
        response = self.client.post(reverse("login"), {
            "username": "user",
            "password": "wrong"
        })
        self.assertNotEqual(response.status_code, 302)

    def test_logout(self):
        user = User.objects.create_user(username="user", password="123")
        self.client.login(username="user", password="123")
        response = self.client.post(reverse("logout"))
        self.assertEqual(response.status_code, 302)
