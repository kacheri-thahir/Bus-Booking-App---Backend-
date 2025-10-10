from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Bus(models.Model):
    bus_name = models.CharField(max_length=300)
    number=models.CharField(max_length=20,unique=True)
    origin=models.CharField(max_length=50)
    destination=models.CharField(max_length=50)
    features=models.TextField()
    no_of_seats=models.PositiveBigIntegerField(null=False,blank=False)
    start_time=models.TimeField()
    reach_time=models.TimeField()
    price=models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return f"{self.bus_name}-{self.number}-{self.origin}-{self.destination}" 


class Seat(models.Model):
    bus=models.ForeignKey(Bus,on_delete=models.CASCADE,related_name='seats')
    Seat_number=models.CharField(max_length=10)
    is_booked=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.bus}-{self.Seat_number}"
    

class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bus=models.ForeignKey(Bus,on_delete=models.CASCADE)
    seat=models.ForeignKey(Seat,on_delete=models.CASCADE)
    booked_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.bus.bus_name}-{self.seat.Seat_number}-{self.booked_time}-{self.bus.origin}-{self.bus.destination}"
    
    
