from django.db import models
from datetime import datetime

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    date = models.DateTimeField()
    
    def __str__(self):
        return f'''{self.name} | {self.date.strftime("%b %d, %Y - %H:%M")} | {self.no_of_guests}'''
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'