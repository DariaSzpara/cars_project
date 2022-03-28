"""cars_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

    
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),    
    path('api/', include('cars.urls')),
     path('api/', include('rates.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

'''
response = requests. get('https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/Volkswagen?format=json')
if (response.status_code != requests.codes.ok):
    print ('Coś poszło nie tak')
else:
    print ('response.json') 

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

'''