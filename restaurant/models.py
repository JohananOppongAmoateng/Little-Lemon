from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    num_of_guest = models.PositiveIntegerField()
    booking_date = models.DateTimeField()


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField()
