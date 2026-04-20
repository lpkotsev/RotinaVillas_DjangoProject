from django import forms
from datetime import date
from django.conf import settings
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
                'class': 'form-control',
                'min': 1
            }),
        }

    def __init__(self, *args, **kwargs):
        self.villa = kwargs.pop("villa", None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        check_in = cleaned_data.get("check_in")
        check_out = cleaned_data.get("check_out")

        if check_in and check_out:


            if check_out <= check_in:
                raise forms.ValidationError(
                    "Check-out must be after check-in."
                )


            if not settings.DEBUG:
                if check_in < date.today():
                    raise forms.ValidationError(
                        "Check-in cannot be in the past."
                    )


            if self.villa:
                overlapping = Booking.objects.filter(
                    villa=self.villa,
                    check_in__lt=check_out,
                    check_out__gt=check_in,
                )

                if overlapping.exists():
                    raise forms.ValidationError(
                        "This villa is already booked for those dates."
                    )

        return cleaned_data



class BookingEditForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out', 'guests']