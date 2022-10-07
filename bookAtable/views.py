from django.shortcuts import render
from .models import Table, Reservation
from django.views import generic, View
from .forms import AvailbilityForm
from bookAtable.reservation_function.avalible import check_available
# from .forms import ReservTableform


class ReservationList(generic.CreateView):
    model = Reservation
    template_name = "reservation_list.html"
    fields = '__all__'


class TableList(generic.CreateView):
    model = Table
    template_name = "table_list.html"
    fields = '__all__'


class ReservationView(generic.FormView):
    form_class = AvailbilityForm
    template_name = 'availbility_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        table_list = Table.objects.filter(seats=data['table_seats'])
        available_tables = []
        for table in table_list:
            if check_available(table, data['arriving_time'], data['leaving_time']):
                available_tables.append(table)

        if len(available_tables) > 0:
            table = available_tables[0]
            reservation = Reservation.objects.create(
                costumer=request.costumer,
                table=table,
                arriving_time=data['arriving_time'],
                leaving_time=data['leaving_time']
            )
        reservation.save()
        return HttpResponse(reservation)
