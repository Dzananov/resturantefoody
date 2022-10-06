from django.shortcuts import render
from .models import Table
from django.views import generic, View
# from .forms import ReservTableform


# class TableList(generic.ListView):
#     model = Table


# class ReservationList(generic.ListView):
#     model = Reservation

class TableList(generic.CreateView):
    model = Table
    template_name = "table_list.html"
    fields = '__all__'
