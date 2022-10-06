from . import views
from django.urls import path


urlpatterns = [
    path('', views.ReservationList.as_view(), name='ReservationList'),
    path('', views.TableList.as_view(), name='TableList')
]
