from django import forms
from .models import Reservation


class BookingForm(forms.ModelForm):
    name = forms.CharField(forms.TextInput(attrs={'placeholder':'Name'})
    )
    email = forms.EmailField(forms.TextInput(attrs={'placeholder'= 'Email'})
    )

    class Meta:
        model = Reservation
        widgets = {
            'date': DateInput(),
        }

 
