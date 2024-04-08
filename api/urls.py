from django.urls import path
from rest_framework import routers
from .views import WeatherForecastView

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('weather-forecast/<str:place>', WeatherForecastView.as_view(), name='weather_forecast'),
]