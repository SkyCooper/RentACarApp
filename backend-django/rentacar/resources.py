from import_export import resources
from .models import Reservation

class ReservationResource(resources.ModelResource):

    class Meta:
        model = Reservation # default all fields
        # fields = ("is_released", "product")