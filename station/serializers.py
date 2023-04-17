from rest_framework import serializers
from .models import Region, District, Station, SunEnergy, WaterEnergy, WindEnergy, DiselEnergy, AccumulatorEnergy

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    class Meta:
        model = District
        fields = '__all__'

class StationSerializer(serializers.ModelSerializer):
    district = DistrictSerializer()
    class Meta:
        model = Station
        fields = '__all__'

class SunEnergySerializer(serializers.ModelSerializer):
    station = StationSerializer()
    class Meta:
        model = SunEnergy
        fields = '__all__'

class WaterEnergySerializer(serializers.ModelSerializer):
    station = StationSerializer()
    class Meta:
        model = WaterEnergy
        fields = '__all__'

class WindEnergySerializer(serializers.ModelSerializer):
    station = StationSerializer()
    class Meta:
        model = WindEnergy
        fields = '__all__'

class DiselEnergySerializer(serializers.ModelSerializer):
    station = StationSerializer()
    class Meta:
        model = DiselEnergy
        fields = '__all__'

class AccumulatorEnergySerializer(serializers.ModelSerializer):
    station = StationSerializer()
    class Meta:
        model = AccumulatorEnergy
        fields = '__all__'