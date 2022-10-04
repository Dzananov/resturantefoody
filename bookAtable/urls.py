from . import views
from django.urls import path


urlpatterns = [
    path('', views.ReservationList.as_view(), name='home'),
    path('book_table', views.BookAtable.as_view(), name='book_table')
]
