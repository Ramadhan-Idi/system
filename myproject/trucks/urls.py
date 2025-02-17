from django.urls import path
from .views import index, trucks_list, contact  # Match function name exactly

urlpatterns = [
    path('regulation/', index, name='regulation'),
    path('', trucks_list, name='truck_list'),  # Use 'trucks_list'
     path('contact/', contact, name='contact'),
      path('base/', contact, name='base'),
]
