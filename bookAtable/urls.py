from . import views
from django.urls import path


urlpatterns = [
    path('table_list/', views.TableList.as_view(), name='table_list'),
    path('reservation_list/', views.ReservationList.as_view(), name='reservation_list'),
    path('reservation/', views.ReservationView.as_view(), name='reservation_view'),
]
