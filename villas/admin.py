from django.contrib import admin
from .models import Villa, Amenity


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Villa)
class VillaAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "price_per_night")
    filter_horizontal = ("amenities",)
