from rest_framework import urlpatterns
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .views import RateViewSet

router = DefaultRouter()
router.register('rates', RateViewSet, basename='rates')

urlpatterns = [] + router.urls