from django.urls import path
from . import views

urlpatterns = [
    path('regions/', views.RegionList.as_view(), name='region-list'),
    path('regions/<int:pk>/', views.RegionDetail.as_view(), name='region-detail'),
    path('districts/', views.DistrictList.as_view(), name='district-list'),
    path('districts/<int:pk>/', views.DistrictDetail.as_view(), name='district-detail'),
    path('stations/', views.StationList.as_view(), name='station-list'),
    path('stations/<int:pk>/', views.StationDetail.as_view(), name='station-detail'),
    path('sun-energies/', views.SunEnergyList.as_view(), name='sun-energy-list'),
    path('sun-energies/<int:pk>/', views.SunEnergyDetail.as_view(), name='sun-energy-detail'),
    path('water-energies/', views.WaterEnergyList.as_view(), name='water-energy-list'),
    path('water-energies/<int:pk>/', views.WaterEnergyDetail.as_view(), name='water-energy-detail'),
    path('wind-energies/', views.WindEnergyList.as_view(), name='wind-energy-list'),
    path('wind-energies/<int:pk>/', views.WindEnergyDetail.as_view(), name='wind-energy-detail'),
    path('disel-energies/', views.DiselEnergyList.as_view(), name='disel-energy-list'),
    path('disel-energies/<int:pk>/', views.DiselEnergyDetail.as_view(), name='disel-energy-detail'),
    path('accumulator-energies/', views.AccumulatorEnergyList.as_view(), name='accumulator-energy-list'),
    path('accumulator-energies/<int:pk>/', views.AccumulatorEnergyDetail.as_view(), name='accumulator-energy-detail'),
]