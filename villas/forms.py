from django import forms
from .models import Villa


class VillaCreateForm(forms.ModelForm):

    class Meta:
        model = Villa
        fields = [
            "name",
            "description",
            "price_per_night",
            "location",
            "villa_type",
            "capacity",
            "image_url",
        ]
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
class VillaSearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        label="Search",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by name or location",
            "class": "form-control"
        })
    )

class VillaFilterForm(forms.Form):
    check_in = forms.DateField(
        required=False,
        label="Check-in",
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "form-control"
        })
    )

    check_out = forms.DateField(
        required=False,
        label="Check-out",
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "form-control"
        })
    )

    min_price = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    max_price = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    guests = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    ordering = forms.ChoiceField(
        required=False,
        label="Sort by",
        choices=[
            ("", "Default"),
            ("name", "Title A → Z"),
            ("-name", "Title Z → A"),
            ("location", "Location A → Z"),
            ("-location", "Location Z → A"),
            ("price_per_night", "Price Low → High"),
            ("-price_per_night", "Price High → Low"),
        ],
        widget=forms.Select(attrs={"class": "form-control"})
    )