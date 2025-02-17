from django.contrib import admin
from .models import Truck

@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'current_weight', 'average_weight', 'status')
