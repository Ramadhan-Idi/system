from django.shortcuts import render
from .models import Truck

def index(request):
    return render(request, 'regulation.html')
def base(request):
    return render(request, 'base.html')

def trucks_list(request):  # Function name has 's'
    trucks = Truck.objects.all()
    return render(request, 'truck.html', {'trucks': trucks})

def contact(request):
    return render(request, 'contact.html')


