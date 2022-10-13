from django.test import TestCase

# Create your tests here.
#Testing to check avalibility
def get_avalible_bookings():
    return {(guests, time) for time in dict(TIME_FRAME).keys() for day in dict(GUESTS).keys()}
#Testing the boo_table view, here it is not finished#
class book_a_Table(generic.ListView):

    model = Reservation
    template_name = "booking_form.html"
    if request.method == 'POST':
        form_class = BookingForm(data=request.POST)
        if form.is_valid():
            BookingForm = form.save()

#This is the finished view. But not working so testing#
class book_a_Table(View):
    """This shows the bookingform if user is loged in. """
    # model = Reservation
    # template_name = "booking_form.html"
    def booking(request):
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

  def booking(request):
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
