from django.shortcuts import render, redirect
from .models import Reservation
from django.views import generic, View
from .forms import BookingForm

# from .forms import ReservTableform

# Homepage is a simple page with e menu section where user can redirect further


def home(request):
    return render(request, 'index.html')

# When user goes to book a table he/she first of all must sign up to an accuont. Fuction redirects user to
# my bookingpage if the form is valid


class book_a_Table(generic.CreateView):
    model = Reservation
    template_name = 'booking_form.html'
    fields = '__all__'
    # def booking(request):
    #     if request.method == 'POST':
    #         form_class = BookingForm(data=request.POST)
    #         return render(request, 'booking_form*')
    #         if form.is_valid():
    #             BookingForm = form.save(commit=False)
    #             messages.success(request, 'Confirmed Booking')
    #             return redirect('my_page')
    #         else:
    #             messages.error(request, 'Error in Booking')
    #             return redirect(book_a_Table)
# class my_page(generic.ListView):

# class ReservationView(generic.FormView):
#   form_class = AvailbilityForm
#   template_name = 'booking_form.html'
#   model = Reservation
