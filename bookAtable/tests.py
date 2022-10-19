from django.test import TestCase




#This is the finished view. But not working so testing

    def first_look_if_booking_works(self):
        if request.method == 'POST':
            form_class = BookingForm(data=request.POST)
            queryset = Reservation.objects.filter
            if form.is_valid():
                BookingForm = form.save(commit=False)
                messages.success(request, 'Confirmed Booking')
                return redirect('my_page')
            else:
                messages.error(request, 'Error in Booking')
                return redirect(book_a_Table)
#That did not even render the view at tempalet#
# with new code I want to show a page where user is told to log in/sign up to book a table #

    def see_if_booking_works(self):
        if request.method == 'POST':
           form = BookingForm(data=request.POST)
            if form.is_valid():
                booking_form = form.save(commit=False)
                booking_form.user = request.user
                booking_form.save()
                messages.success(request, 'Confirmed Booking')
                return redirect('my_page')
            else:
                messages.error(request, 'Error in Booking')
                return redirect(book_a_Table)
