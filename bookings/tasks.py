from celery import shared_task
from django.core.mail import send_mail
from django.utils.timezone import now
from datetime import timedelta
from .models import Booking


@shared_task
def send_booking_confirmation_async(email, villa_name):
    send_mail(
        subject="Booking Confirmed",
        message=f"You successfully booked {villa_name}.",
        from_email="no-reply@rotinavillas.com",
        recipient_list=[email],
        fail_silently=True,
    )


@shared_task
def delete_old_bookings():
    five_years_ago = now() - timedelta(days=5 * 365)

    deleted_count, _ = Booking.objects.filter(
        check_out__lt=five_years_ago
    ).delete()

    print(f"Deleted {deleted_count} old bookings")