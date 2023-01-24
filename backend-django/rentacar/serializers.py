from rest_framework import serializers
from .models import Reservation, Customer, Car

class ReservationSerializer(serializers.ModelSerializer):
    car = serializers.StringRelatedField()
    customer = serializers.StringRelatedField()
    reserved_days = serializers.SerializerMethodField()
    class Meta:
        model = Reservation
        fields = ("id", "car", "customer", "start_date", "end_date", "reserved_days")
        
    def get_reserved_days(self, obj):
        return obj.end_date.day - obj.start_date.day
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("id", "first_name", "last_name")
        
class CarSerializer(serializers.ModelSerializer):
    # rent_per_day = serializers.StringRelatedField()
    class Meta:
        model = Car
        fields = ("id", "plate_number", "brand", "model",
                  "year", "gear", "fuel", "rent_per_day",
                  "availibity")