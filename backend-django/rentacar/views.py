from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class ReservationMVS(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    
class CustomerMVS(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class CarMVS(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    