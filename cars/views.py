from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from cars.models import Car
from cars.serializers import CarsSerializer


class CarsViewSet(ReadOnlyModelViewSet):
    queryset = Car.objects.all() 
    serializer_class = CarsSerializer

''''''
class CarsList(APIView):
    """
    List all cars, or create a new cars.
    """
    def get(self, request, format=None):
        cars = Car.objects.all()
        serializer = CarsSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()


response = requests. get('https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/Volkswagen?format=json')
if (response.status_code != requests.codes.ok):
    print ('Coś poszło nie tak')
else:
    print (response.json()) 

"""
    requestCar = {
        'make' : 'Make_Name',
        'model' ; 'Model_Name',

    }     
"""
       
response = requests. post('https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/Volkswagen?format=json')
if (response.status_code != requests.codes.created):
    print ('Coś poszło nie tak')
else:
    print (response.json())