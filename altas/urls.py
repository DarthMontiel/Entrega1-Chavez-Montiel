from django.urls import path
from altas.views import *

urlpatterns = [
    path("",inicio,name="inventario-inicio"), #URL de INICIO
    path("licencias/",licencias,name="inventario-licencias"), #URL de LICENCIAS
    path("alta_licencias/",licencias_alta,name="inventario-licencias-alta"),#URL de Alta nueva licencia

]