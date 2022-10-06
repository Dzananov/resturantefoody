from django.shortcuts import render
from .models import Table, Reservation
from django.views import generic
# from .forms import ReservTableform


class TableList(generic.Listview):
    model = Table


class ReservationList(generic.ListView):
    model = Reservation
