from django.shortcuts import render

# Create your views here.

# authenticate , permissions , token , status , response , generics , apiview

from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from.serializers import UserRegisterSerializer,BusSerializer,SeatSerializer,BookingSerializer
from .models import Bus,Seat,Booking


# for user registration 
class UserRegistrationView(APIView):
    def post(self,request):
        serializer=UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token,created=Token.objects.get_or_create(user=user)           #whenever new user registered a token will be generated
            return Response({'token':token.key},status=status.HTTP_201_CREATED)     
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    def post(self,request):
        username=request.data.get('username')   #request.data is DRF’s version of request body data (collects data from user)
        password=request.data.get('password')   #request.data is DRF’s version of request body data (collects data from user)
        user=authenticate(username=username,password=password)
        if user:
            token,created=Token.objects.get_or_create(user=user)
            return Response({
                'token':token.key,
                'user_id':user.id,
            },status=status.HTTP_200_OK)
        return Response({'error':'INVALID CREDENTIALS'},status=status.HTTP_401_UNAUTHORIZED)
    

class BusListCreateview(generics.ListCreateAPIView):
    queryset=Bus.objects.all()
    serializer_class=BusSerializer

class BusDetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset=Bus
    serializer_class=BusSerializer
        

class BookingView(APIView):
    permission_classes=[IsAuthenticated]        #checks if user is authenticated

    def post(self,request):
        seat_id=request.data.get('seat')        #request.data is DRF’s version of request body data (collects data from user)
        try:
            seat=Seat.objects.get(id=seat_id)
            if seat.is_booked:
                return Response({'error':'SEAT ALREADY BOOKED!!'},status=status.HTTP_400_BAD_REQUEST)
            seat.is_booked=True     #if seat is not booked
            seat.save()

            bookings=Booking.objects.create(
                user=request.user,
                bus=seat.bus,
                seat=seat
            )
            serializer=BookingSerializer(bookings)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        except seat.DoesNotExist:
            return Response({'error':'INVALID SEAT ID'},status=status.HTTP_400_BAD_REQUEST)
        
# user-specific booking view, where you only allow an authenticated user to see their own bookings
class userbookingview(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request,user_id):
        if request.user.id != user_id:
            return Response({'error':'UN AUTHORIZED'},status=status.HTTP_401_UNAUTHORIZED)
        bookings=Booking.objects.filter(user_id=user_id)
        serializer=BookingSerializer(bookings,many=True)
        return Response(serializer.data)

# each bus seats :

class SeatListView(APIView):
    def get(self,request,bus_id):
        seats=Seat.objects.filter(bus_id=bus_id)
        serializer=SeatSerializer(seats,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    


