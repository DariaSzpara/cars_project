from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rates.models import Rate
from rates.serializers import RateSerializer

# Create your views here.

class RateViewSet(ReadOnlyModelViewSet):
    queryset = Rate.objects.all() 
    serializer_class = RateSerializer

class RatesCreateList(APIView):
    def post(self, request, format=None):
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

