from django.db import models
from django.contrib.auth.models import User

class ParkingSpot(models.Model):
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('Available', 'Available'), ('Occupied', 'Occupied')])

    def __str__(self):
        return self.location

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"Reservation by {self.user.username} for {self.parking_spot.location}"

class Payment(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('Paid', 'Paid'), ('Pending', 'Pending')])

    def __str__(self):
        return f"Payment for {self.reservation} - {self.status}"
