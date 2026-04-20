from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

class AppUser(AbstractUser):
    pass

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    instagram = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username