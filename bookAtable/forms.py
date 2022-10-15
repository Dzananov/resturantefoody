from django import forms


GUESTS = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
)
TIME_FRAME = (
    (1, '16-17'),
    (2, '17-18'),
    (3, '18-19'),
    (3, '19-20'),
)


class BookingForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    guests = forms.ChoiceField(choices=GUESTS, required=True)
    time = forms.ChoiceField(choices=TIME_FRAME, required=True)
    date = forms.DateField(required=True, input_formats=['%y-%m-%d'])
