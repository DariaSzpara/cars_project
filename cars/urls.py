from rest_framework import urlpatterns
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .views import CarsViewSet

router = DefaultRouter()
router.register('cars', CarsViewSet, basename='cars')

urlpatterns = [] + router.urls