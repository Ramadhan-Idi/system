from django.shortcuts import render
from .models import Truck
import json
def index(request):
    return render(request, 'regulation.html')
def base(request):
    return render(request, 'base.html')

def trucks_list(request):
    trucks = Truck.objects.all()
    
    # Get overloaded trucks (those exceeding 48 tons)
    overloaded_trucks = Truck.objects.filter(current_weight__gte=48).values("license_plate")

    return render(request, 'truck.html', {
        'trucks': trucks,
        'overloaded_trucks': json.dumps(list(overloaded_trucks))  # Convert queryset to JSON
    })

def contact(request):
    return render(request, 'contact.html')


