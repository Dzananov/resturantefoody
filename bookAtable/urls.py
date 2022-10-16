from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('booking/', views.book_a_Table, name='booking'),
    path('my_page/', views.my_page, name='my_page'),
    ]
# path('reservation/', views.ReservationView.as_view(), name='reservation_view'),
# path('reservation_list/', views.ReservationList.as_view(), name='reservation_list'),
