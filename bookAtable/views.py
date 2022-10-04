from django.shortcuts import render
from .models import Reservations
from django.views import generic


class ReservationList(generic.ListView):
    model = Reservations
    template_name = 'index.html'


class BookAtable(generic.CreateView):
    model = Reservations
    template_name = 'book_table.html'
    fields = '__all__'

