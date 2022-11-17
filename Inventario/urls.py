from django.urls import path #Importamos Path
from Inventario.views import * #Importamos todas las vistas


#El archivo debe tener un archivo llamado exactamente urlpattern
urlpatterns = [
    path("",inicio, name="inventario-inicio"),
    path("alta_laptop/",alta_laptop,name="alta_laptop"),
]