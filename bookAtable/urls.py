from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('booking/', views.book_a_Table, name='booking'),
    path('my_page/', views.my_page, name='my_page'),
    path('edit/<booking_id>', views.edit_bookings, name='edit'),
    path('delete/<booking_id>', views.delete_booking, name='delete'),
    path('menu/', views.menu, name='menu'),
    ]
