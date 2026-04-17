from django.db import models
from villas.models import Villa
from django.contrib.auth import get_user_model

User = get_user_model()

class Review(models.Model):
    villa = models.ForeignKey("villas.Villa", on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ✅ ADD THIS
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    guest_name = models.CharField(max_length=100)

    rating = models.IntegerField(
        choices=[(1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5")]
    )

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.villa} - {self.rating}"

# Create your models here.
