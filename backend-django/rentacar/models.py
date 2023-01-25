from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    customer_id = models.BigIntegerField()

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    
class Car(models.Model):
    
    GEAR = (
        ("Auto", "Automatic"),
        ("Manuel", "Manual"),)

    FUEL = (
        ("Diesel ", "Diesel"),
        ("Petrol", "Petrol"),
        ("Hybrid", "Hybrid"),
        ("Electric", "Electric"),
        ("LPG", "LPG"),)
    
    BRAND = (
        ("Mercedes", "Mercedes"),
        ("BMW", "BMW"),
        ("Audi", "Audi"),
        ("Toyota", "Toyota"),
        ("Nissan", "Nissan"),)
    
    PRICE = (
        (1, 250),
        (2, 500),
        (3, 800),
        (4, 1000),)
    
    YEAR = (
        (2021, 2021),
        (2022, 2022),
        (2023, 2023),
        (2024, 2024),)
    
    plate_number = models.CharField(max_length=15, null=True, blank=True)
    brand = models.CharField(max_length=15, choices=BRAND)
    model = models.CharField(max_length=15)
    year = models.SmallIntegerField(choices=YEAR)
    gear = models.CharField(max_length=10, choices=GEAR)
    fuel = models.CharField(max_length=10, choices=FUEL)
    rent_per_day = models.IntegerField(choices=PRICE)
    availibity = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return f"{self.brand}/{self.model} - {self.year}"
    
class Reservation (models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="reservations")
    
    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"
    
    def __str__(self):
        return f"Customer {self.customer} reserved {self.car}"