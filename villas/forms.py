from django import forms
from .models import Villa


class VillaCreateForm(forms.ModelForm):

    class Meta:
        model = Villa
        exclude = ("created_at",)
        labels = {
            "price_per_night": "Price per night (€)"
        }
        help_texts = {
            "capacity": "Maximum number of guests"
        }


class VillaEditForm(forms.ModelForm):

    created_at = forms.DateTimeField(
        label="Created at",
        disabled=True,
        required=False
    )

    class Meta:
        model = Villa
        fields = [
            "name",
            "location",
            "description",
            "price_per_night",
            "capacity",
            "image_url",
            "villa_type",
            "amenities",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance:
            self.fields["created_at"].initial = self.instance.created_at