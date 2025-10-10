from django.contrib import admin
from .models import Bus,Seat,Booking
# Register your models here.


class BusAdmin(admin.ModelAdmin):
    list_display=('bus_name','number','origin','destination')
    search_fields=('bus_name','number','origin')

class SeatAdmin(admin.ModelAdmin):
    list_display=('bus','Seat_number')

class BookingAdmin(admin.ModelAdmin):
    list_display=('user','bus')
    search_fields=('bus','seat')

admin.site.register(Bus,BusAdmin)
admin.site.register(Seat,SeatAdmin)
admin.site.register(Booking,BookingAdmin)
