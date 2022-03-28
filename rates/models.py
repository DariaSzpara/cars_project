from django.db import models
from cars.models import Car

from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Rate(models.Model):
    rating =  models.IntegerField(validators=[MinValueValidator(10),
                                            MaxValueValidator(500)])
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='rates') 

    