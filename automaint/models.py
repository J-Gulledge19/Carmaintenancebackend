from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=20, unique=True)
    image = models.CharField(max_length=400)
    
    def __str__(self):
        return self.name
    
class Maint(models.Model):
    type = models.CharField(max_length=50)
    date = models.CharField(max_length=20)
    mileage = models.CharField(max_length=10)
    due = models.CharField(max_length=20)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='maintenance')
    
    def __str__(self):
        return self.type