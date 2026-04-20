from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Avg

User = get_user_model()


class Review(models.Model):
    villa = models.ForeignKey(
        "villas.Villa",
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField(
        choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]
    )

    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("villa", "user")

    def __str__(self):
        return f"{self.villa} - {self.rating}"