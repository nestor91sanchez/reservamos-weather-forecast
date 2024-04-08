from rest_framework import serializers

class ForecastSerializer(serializers.Serializer):
    dt = serializers.CharField()
    min_temp = serializers.FloatField()
    max_temp = serializers.FloatField()

class CityForecastSerializer(serializers.Serializer):
    display = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    country = serializers.CharField()
    forecast = serializers.DictField(child=ForecastSerializer())

class WeatherForecastResponseSerializer(serializers.Serializer):
    cities = serializers.ListField(child=CityForecastSerializer())