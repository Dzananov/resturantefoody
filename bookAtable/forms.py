from django import forms
from .models import Reservation


# GUESTS = (
#     (1, '1'),
#     (2, '2'),
#     (3, '3'),
#     (4, '4'),
#     (5, '5'),
#     (6, '6'),
# )
# TIME_FRAME = (
#     (1, '16-17'),
#     (2, '17-18'),
#     (3, '18-19'),
#     (3, '19-20'),
# )


class BookingForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

