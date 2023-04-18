from rest_framework import serializers
from .models import Region, District, Station, SunEnergy, WaterEnergy, WindEnergy, DiselEnergy, AccumulatorEnergy

class SunEnergySerializer(serializers.ModelSerializer):

    class Meta:
        model = SunEnergy
        fields = '__all__'

class WaterEnergySerializer(serializers.ModelSerializer):

    class Meta:
        model = WaterEnergy
        fields = '__all__'

class WindEnergySerializer(serializers.ModelSerializer):

    class Meta:
        model = WindEnergy
        fields = '__all__'

class DiselEnergySerializer(serializers.ModelSerializer):

    class Meta:
        model = DiselEnergy
        fields = '__all__'

class AccumulatorEnergySerializer(serializers.ModelSerializer):

    class Meta:
        model = AccumulatorEnergy
        fields = '__all__'

class StationSerializer(serializers.ModelSerializer):
    sun_energies = SunEnergySerializer(many=True, read_only=True)
    water_energies = WaterEnergySerializer(many=True, read_only=True)
    wind_energies = WindEnergySerializer(many=True, read_only=True)
    disel_energies = DiselEnergySerializer(many=True, read_only=True)
    accumulator_energies = AccumulatorEnergySerializer(many=True, read_only=True)

    class Meta:
        model = Station
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    stations = StationSerializer(many=True, read_only=True)

    class Meta:
        model = District
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    districts = DistrictSerializer(many=True, read_only=True)

    class Meta:
        model = Region
        fields = '__all__'


