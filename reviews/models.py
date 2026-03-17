from django.db import models
from villas.models import Villa


class Review(models.Model):

    villa = models.ForeignKey(
        Villa,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    guest_name = models.CharField(max_length=100)

    rating = models.IntegerField(
        choices=[(1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5")]
    )

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.villa} - {self.rating}"

# Create your models here.
