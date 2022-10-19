from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from django.views import generic, View
from .forms import BookingForm
from django.http import HttpResponseRedirect
from django.contrib import messages


""" Homepage is a simple page with e menu section where user can redirect further. Function that shows homepage"""


def home(request):
    return render(request, 'index.html')


"""This function will enable bookings for signed in users. If user is signed in will be checked trough the template. the booking
will be renderd to The My bookings page"""


def book_a_Table(request):
    if request.method == 'POST':
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form = booking_form.save(commit=False)
            booking_form.user = request.user
            booking_form.save()
            messages.success(request, 'Booking is Complete')
            return redirect('my_page')
        else:
            messages.error(request, 'Check if all the fields are filled and or you are trying to add a double booking')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'booking_form.html', context)


"""Here is the view function for the bookings that is made"""


def my_page(request):
    if request.user.is_authenticated:
        model = Reservation
        bookings = Reservation.objects.filter(costumer=request.user)
        context = {
            'bookings': bookings
        }
        return render(request, 'mybookings.html', context)


"""The user can edit bookings and save the changes to the My Booking page"""


def edit_bookings(request, booking_id):
    booking = get_object_or_404(Reservation, id=booking_id)
    if request.method == 'POST':
        booking_form = BookingForm(request.POST, instance=booking)
        if booking_form.is_valid():
            booking_form.user = request.user
            booking_form.save()
            messages.success(request, 'Booking is Complete')
            return redirect('my_page')
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'edit_booking.html', context)


"""The user can delete bookings and they will disappear"""


def delete_booking(request, booking_id):
    booking = get_object_or_404(Reservation, id=booking_id)
    booking.delete()
    return redirect('my_page')
