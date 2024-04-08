import requests
from requests.exceptions import HTTPError
from django.conf import settings


def get_places(place):
    try:
        url = f"https://search.reservamos.mx/api/v2/places?q={place}"
        response = requests.get(url, headers={'Accept': 'application/json'} , timeout=10)
        result = response.json()
    except HTTPError as e:
        result = []
    return result

def get_weather_forecast(place):
    try:
        api_key = settings.OPENWEATHER_API_KEY
        url = f"https://api.openweathermap.org/data/2.5/onecall?lat={place['lat']}&lon={place['long']}&exclude=minute,hourly&appid={api_key}"
        response = requests.get(url, headers={'Accept': 'application/json'} , timeout=10)
        result = response.json()
    except HTTPError as e:
        result = []
    return result