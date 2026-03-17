from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    check_in = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )

    check_out = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = Booking
        fields = [
            "guest_name",
            "guest_email",
            "check_in",
            "check_out",
            "guests",
        ]

    def clean(self):
        cleaned_data = super().clean()

        check_in = cleaned_data.get("check_in")
        check_out = cleaned_data.get("check_out")

        if check_in and check_out:
            if check_out <= check_in:
                raise forms.ValidationError(
                    "Check-out date must be after check-in date."
                )



        return cleaned_data

