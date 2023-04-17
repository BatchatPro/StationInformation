from django.contrib import admin
from .models import Region, District, Station, SunEnergy, WaterEnergy, WindEnergy, DiselEnergy, AccumulatorEnergy

admin.site.register(Region)
admin.site.register(District)
admin.site.register(Station)
admin.site.register(SunEnergy)
admin.site.register(WaterEnergy)
admin.site.register(WindEnergy)
admin.site.register(DiselEnergy)
admin.site.register(AccumulatorEnergy)
