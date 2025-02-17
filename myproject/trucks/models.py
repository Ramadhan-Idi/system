from django.db import models

class Truck(models.Model):
    license_plate = models.CharField(max_length=20, unique=True)
    current_weight = models.FloatField()
    average_weight = models.FloatField()

    def status(self):
        return "Overloading" if self.current_weight >= 48 else "Normal"

    def status_color(self):
        return "red" if self.current_weight >= 48 else "green"

    def __str__(self):
        return f"Truck {self.license_plate}"
