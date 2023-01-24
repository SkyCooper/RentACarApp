from django.urls import path,include
from rest_framework import routers
from .views import ReservationMVS, CustomerMVS, CarMVS

router = routers.DefaultRouter()
router.register("reservation", ReservationMVS)
router.register("customer", CustomerMVS)
router.register("car", CarMVS)

urlpatterns = router.urls
