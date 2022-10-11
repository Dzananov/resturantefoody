from django.shortcuts import render, HttpResponse
from .models import Reservation
from django.views import generic, View
from .forms import BookingForm
from bookAtable.reservation_function.avalible import check_available
# from .forms import ReservTableform


def home(request):
    return(request, 'index.html')


def book_a_Table(request):
    model = Table
    template_name = "table_list.html"
    fields = '__all__'


class ReservationView(generic.FormView):
    form_class = AvailbilityForm
    template_name = 'availbility_form.html'
    model = Reservation

    def AvailbilityForm():
        Table.objects.filter(table=table, arriving_time=arriving_time).annotate(
            is_booked_on=Exists(Reservation.objects.filter(table_avaibility=OutRef('pk'), date=date)
            )
            ).filter(is_booked_on=False)

