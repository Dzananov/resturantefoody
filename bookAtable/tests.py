from django.test import TestCase

# Create your tests here.
def get_avalible_bookings():
    return {(guests, time) for time in dict(TIME_FRAME).keys() for day in dict(GUESTS).keys()}