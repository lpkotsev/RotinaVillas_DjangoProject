from django.db import models
from villas.models import Villa
from django.conf import settings

class Booking(models.Model):

    villa = models.ForeignKey(
        Villa,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    guest_name = models.CharField(max_length=100)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    guest_email = models.EmailField()

    check_in = models.DateField()

    check_out = models.DateField()

    guests = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.guest_name} - {self.villa}"

# Create your models here.
