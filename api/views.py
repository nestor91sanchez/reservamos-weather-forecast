import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import WeatherForecastResponseSerializer
from .services import get_places, get_weather_forecast
from django.http import JsonResponse

class WeatherForecastView(APIView):
    def get(self, request, place):
        places = get_places(place)
        if len(places) > 0:
            forecast_data = []
            for place in places:
                weather_data = get_weather_forecast(place)
                if 'daily' in weather_data:
                    current_data = [{"display": place['display'], "city": place['city_slug'], "state": place['state'], "country": place['country'],"forecast": []}]
                    for day in weather_data['daily'][:7]:
                        current_data[0]['forecast'].append({
                            "dt": day['dt'],
                            "max_temp": day['temp']['max'],
                            "min_temp": day['temp']['min'],
                        })
                    forecast_data.append(current_data[0])

            # serializer = WeatherForecastResponseSerializer(forecast_data, many=True)
            # return Response(serializer)
            return JsonResponse(forecast_data, safe=False)
        else:
            return Response({"error": "Place not found"}, status=404)