from django.contrib import admin
from .models import Reservation, Customer, Car

# Register your models here.
admin.site.register(Reservation)
admin.site.register(Customer)
admin.site.register(Car)