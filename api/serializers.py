from rest_framework import serializers
from villas.models import Villa
from reviews.models import Review
from bookings.models import Booking

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["rating", "comment"]


class VillaSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Villa
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Booking
        fields = "__all__"