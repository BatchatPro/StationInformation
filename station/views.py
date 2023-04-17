from rest_framework import generics
from .models import Region, District, Station, SunEnergy, WaterEnergy, WindEnergy, DiselEnergy, AccumulatorEnergy
from .serializers import RegionSerializer, DistrictSerializer, StationSerializer, SunEnergySerializer, WaterEnergySerializer, WindEnergySerializer, DiselEnergySerializer, AccumulatorEnergySerializer

class RegionList(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class RegionDetail(generics.RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class DistrictList(generics.ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class DistrictDetail(generics.RetrieveAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class StationList(generics.ListAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

class StationDetail(generics.RetrieveAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

class SunEnergyList(generics.ListAPIView):
    queryset = SunEnergy.objects.all()
    serializer_class = SunEnergySerializer

class SunEnergyDetail(generics.RetrieveAPIView):
    queryset = SunEnergy.objects.all()
    serializer_class = SunEnergySerializer

class WaterEnergyList(generics.ListAPIView):
    queryset = WaterEnergy.objects.all()
    serializer_class = WaterEnergySerializer

class WaterEnergyDetail(generics.RetrieveAPIView):
    queryset = WaterEnergy.objects.all()
    serializer_class = WaterEnergySerializer

class WindEnergyList(generics.ListAPIView):
    queryset = WindEnergy.objects.all()
    serializer_class = WindEnergySerializer

class WindEnergyDetail(generics.RetrieveAPIView):
    queryset = WindEnergy.objects.all()
    serializer_class = WindEnergySerializer

class DiselEnergyList(generics.ListAPIView):
    queryset = DiselEnergy.objects.all()
    serializer_class = DiselEnergySerializer

class DiselEnergyDetail(generics.RetrieveAPIView):
    queryset = DiselEnergy.objects.all()
    serializer_class = DiselEnergySerializer

class AccumulatorEnergyList(generics.ListAPIView):
    queryset = AccumulatorEnergy.objects.all()
    serializer_class = AccumulatorEnergySerializer

class AccumulatorEnergyDetail(generics.RetrieveAPIView):
    queryset = AccumulatorEnergy.objects.all()
    serializer_class = AccumulatorEnergySerializer