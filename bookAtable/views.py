from django.shortcuts import render, redirect
from .models import Reservation
from django.views import generic, View
from .forms import BookingForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# from .forms import ReservTableform

# Homepage is a simple page with e menu section where user can redirect further


def home(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')

# When user goes to book a table he/she first of all must sign up to an account. Fuction redirects user to
# my bookingpage if the form is valid


def book_a_Table(request):
    if request.method == 'POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booking_form.user = request.user
            booking_form.save()
            messages.success(request, 'Booking is Complete')
            return redirect('my_page')
        else:
            messages.error(request, 'Invalid form')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'booking_form.html', context)


def my_page(request):
    if request.user.is_authenticated:
        model = Reservation
        bookings = Reservation.objects.filter(costumer=request.user)
        context = {
            'bookings': bookings
        }
        return render(request, 'mybookings.html', context)

def edit_bookings(request, booking_id):
    booking = get_object_or_404(Reservation, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(data=request.POST, instance=booking)
        if form.is_valid():
            booking_form.user = request.user
            booking_form.save()
            messages.success(request, 'Booking is Complete')
            return redirect('my_page')
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'edit_booking.html', context)
