from rest_framework import serializers
from .models import Bus,Seat,Booking
from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):      #user registrartion , to create new user
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','email','password']

    def create(self, validated_data):                       #to validate the user information 
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user                                         #new user created


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model= Bus
        fields= '__all__'

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model= Seat
        fields= ['id','Seat_number','is_booked']

class BookingSerializer(serializers.ModelSerializer):
    bus=serializers.StringRelatedField()
    seat=SeatSerializer
    user=serializers.StringRelatedField()
    class Meta:
        model=Booking
        fields='__all__'
        read_only=['user','bus','seat','booked_time']