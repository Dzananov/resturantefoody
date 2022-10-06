from . import views
from django.urls import path


urlpatterns = [
    path('table_list/', views.TableList.as_view(), name='table_list'),
    
]
