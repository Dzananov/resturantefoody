from django import forms


class AvailbilityForm(forms.Form):
    TABLE_SEATS = (
        ('Two', '2 SEATS'),
        ('Four', '4 SEATS'),
        ('Eight', '8 SEATS'),
    )
    room_category = forms.ChoiceField(choices=TABLE_SEATS, required=True)
    arriving_time = forms.DateTimeField(required=True)
    leaving_time = forms.DateTimeField(required=True)
