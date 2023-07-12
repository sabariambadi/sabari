from django.db import models
from users.models import User

class Ride(models.Model):
    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides_as_rider')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides_as_driver')
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ride(models.Model):

    def start_ride(self):
        self.status = 'Started'
        self.save()

    def complete_ride(self):
        self.status = 'Completed'
        self.save()

    def cancel_ride(self):
        self.status = 'Cancelled'
        self.save()

class Ride(models.Model):
    current_location = models.CharField(max_length=100)