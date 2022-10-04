from . import views
from django.urls import path


urlpatterns = [
    path('book_table', views.ReservationList.as_view(), name='book_table')
    
]