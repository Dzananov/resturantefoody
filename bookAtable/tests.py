from django.test import TestCase

# Create your tests here.
def get_avalible_bookings():
    return {(guests, time) for time in dict(TIME_FRAME).keys() for day in dict(GUESTS).keys()}
class book_a_Table(generic.ListView):
"""This shows the bookingform if user is loged in. """
    model = Reservation
    template_name = "booking_form.html"
    if request.method == 'POST':
        form_class = BookingForm(data=request.POST)
        if form.is_valid():
            BookingForm= save