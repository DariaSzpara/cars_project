from django.db import models

# Create your models here.

class Car(models.Model):
    model =  models.CharField(max_length=10)
    make = models.CharField(max_length=10)
