from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out', 'guests']

        widgets = {
            'check_in': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'check_out': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'guests': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }
    def clean_guests(self):
        guests = self.cleaned_data["guests"]

        if guests <= 0:
            raise forms.ValidationError("Guests must be at least 1.")

        return guests

        check_in = cleaned_data.get("check_in")
        check_out = cleaned_data.get("check_out")

        if check_in and check_out:
            if check_out <= check_in:
                raise forms.ValidationError(
                    "Check-out date must be after check-in date."
                )



        return cleaned_data

