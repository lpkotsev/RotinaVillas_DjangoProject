from django.db import models
from django.core.validators import MinValueValidator

class Amenity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"


class Villa(models.Model):

    VILLA_TYPES = [
        ("beach", "Beach"),
        ("mountain", "Mountain"),
        ("city", "City"),
    ]

    name = models.CharField(max_length=120)

    location = models.CharField(max_length=120)

    description = models.TextField()

    price_per_night = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(1)]
    )

    capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )


    image_url = models.CharField(max_length=200, blank=True)

    villa_type = models.CharField(
        max_length=20,
        choices=VILLA_TYPES
    )

    amenities = models.ManyToManyField("Amenity", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.location}"

    def average_rating(self):
        ratings = self.reviews.all()

        if ratings.exists():
            return sum(r.rating for r in ratings) / ratings.count()

        return 0


