from . import views
from django.urls import path


urlpatterns = [
    path('booking_form/', views.book_a_Table.as_view(), name='booking_form'),
]
# path('reservation/', views.ReservationView.as_view(), name='reservation_view'),
# path('reservation_list/', views.ReservationList.as_view(), name='reservation_list'),
