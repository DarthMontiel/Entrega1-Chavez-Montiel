from django.db import models

# Create your models here.
class Licencias(models.Model):
    software = models.CharField(max_length=40)
    licencia = models.CharField(max_length=50)
    email = models.EmailField()