from django.db import models


class Region(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name
    

class Station(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    nomi = models.CharField(max_length = 525)
    manizl = models.CharField(max_length = 525)
    telefon = models.CharField(max_length = 125)

    def __str__(self):
        return self.nomi
    

class SunEnergy(models.Model):
    station = models.OneToOneField(Station, on_delete=models.CASCADE)
    nomi = models.CharField(max_length = 255)
    kuchlanish = models.FloatField()
    tok_kuchi = models.FloatField()
    harorat = models.FloatField()
    quvvat = models.FloatField()
    chastota = models.FloatField()

    def __str__(self):
        return self.nomi
    
    
class WaterEnergy(models.Model):
    station = models.OneToOneField(Station, on_delete=models.CASCADE)
    nomi = models.CharField(max_length = 255)
    kuchlanish = models.FloatField()
    tok_kuchi = models.FloatField()
    harorat = models.FloatField()
    quvvat = models.FloatField()
    chastota = models.FloatField()

    def __str__(self):
        return self.nomi
    
    
class WindEnergy(models.Model):
    station = models.OneToOneField(Station, on_delete=models.CASCADE)
    nomi = models.CharField(max_length = 255)
    kuchlanish = models.FloatField()
    tok_kuchi = models.FloatField()
    harorat = models.FloatField()
    quvvat = models.FloatField()
    chastota = models.FloatField()

    def __str__(self):
        return self.nomi
    
    
class DiselEnergy(models.Model):
    station = models.OneToOneField(Station, on_delete=models.CASCADE)
    nomi = models.CharField(max_length = 255)
    kuchlanish = models.FloatField()
    tok_kuchi = models.FloatField()
    harorat = models.FloatField()
    quvvat = models.FloatField()
    chastota = models.FloatField()

    def __str__(self):
        return self.nomi
    
    
class AccumulatorEnergy(models.Model):
    station = models.OneToOneField(Station, on_delete=models.CASCADE)
    nomi = models.CharField(max_length = 255)
    kuchlanish = models.FloatField()
    tok_kuchi = models.FloatField()
    harorat = models.FloatField()
    quvvat = models.FloatField()
    chastota = models.FloatField()

    def __str__(self):
        return self.nomi
    
    


