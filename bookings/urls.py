from django.urls import path
from.views import UserRegistrationView,LoginView,BusListCreateview,BookingView,userbookingview

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('buses/',BusListCreateview.as_view(),name='buses'),
    path('bookings/',BookingView.as_view(),name='bookings'),
    path('user/<int:user_id>/bookinglist/',userbookingview.as_view(),name='userbookings'),
    
]
