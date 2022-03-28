from rest_framework import serializers

from .models import Car

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'model',
            'make',
        
        )