from django import forms


GUESTS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)
TIME_FRAME = (
    ('16-17', '16-17'),
    ('17-18', '17-18'),
    ('18-19', '18-19'),
    ('19-20', '19-20'),
)


class BookingForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    guests = forms.ChoiceField(choices=GUESTS, required=True)
    time = forms.ChoiceField(choices=TIME_FRAME, required=True)
    date = forms.DateField()
