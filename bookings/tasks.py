import threading
import time


def send_booking_confirmation(booking_id):
    # simulate heavy work
    time.sleep(2)

    print(f"Booking {booking_id} confirmed (async task)")


def send_booking_confirmation_async(booking_id):
    thread = threading.Thread(
        target=send_booking_confirmation,
        args=(booking_id,)
    )
    thread.start()