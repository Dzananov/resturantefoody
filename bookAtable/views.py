from django.shortcuts import render
from .models import Reservation
from django.views import generic, View
from .forms import BookingForm

# from .forms import ReservTableform


def home(request):
    return render(request, 'index.html')


class book_a_Table(generic.ListView):
    model = Reservation
    template_name = "booking_form.html"


# class ReservationView(generic.FormView):
#   form_class = AvailbilityForm
#   template_name = 'booking_form.html'
#   model = Reservation
