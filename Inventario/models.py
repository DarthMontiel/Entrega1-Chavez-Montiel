from django.db import models

# Create your models here.
class laptops(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    memoriaRam = models.IntegerField()
    DiscoDuro = models.IntegerField()
    DiscoSSD = models.IntegerField()
    Procesador = models.CharField(max_length=50)

class licencias(models.Model):
    software = models.CharField(max_length=50)
    licencia = models.CharField(max_length=50)
    email = models.EmailField()

class dispMoviles(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ram = models.IntegerField()
    memoria = models.IntegerField()
