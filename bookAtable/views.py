from django.shortcuts import render
from .models import Reservations
from django.views import generic


class ReservationList(generic.ListView):
    model = Reservations
    template_name = 'index.html'


