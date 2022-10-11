from django.shortcuts import render, HttpResponse
from .models import Reservation
from django.views import generic, View
from .forms import BookingForm

# from .forms import ReservTableform


class home(generic.ListView):
    template_name = 'index.html'


class book_a_Table(generic.ListView):
    model = Reservation
    template_name = "booking_form.html"
    fields = '__all__'


# class ReservationView(generic.FormView):
#   form_class = AvailbilityForm
#   template_name = 'booking_form.html'
#   model = Reservation
