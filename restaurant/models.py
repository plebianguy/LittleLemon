from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length = 255)
    no_of_guests = models.IntegerField(validators = [MinValueValidator(0),])
    booking_date = models.DateTimeField()
    
    def __str__(self):
        return f"Booking {self.id} in {self.name}'s name for {self.no_of_guests} people on {self.booking_date}"
    
class MenuItem(models.Model):
    title = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 10, decimal_places= 2)
    inventory = models.PositiveIntegerField()
    
    def get_item(self):
        return f'{self.title} : {str(self.price)}'