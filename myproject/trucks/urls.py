from django.urls import path
from .views import index, trucks_list, contact, dashboard  # Match function name exactly

urlpatterns = [
    path('regulation/', index, name='regulation'),
    path('truck_list/', trucks_list, name='truck_list'),  # Use 'trucks_list'
     path('contact/', contact, name='contact'),
      path('base/', contact, name='base'),
       path('', dashboard, name='dashboard'),
]
