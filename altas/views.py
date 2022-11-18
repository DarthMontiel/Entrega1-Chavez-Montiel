from django.shortcuts import render
from altas.models import *
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "altas/index.html")

#Vistas para licencias
def licencias(request):
    return render(request, "altas/licencia.html")
def licencias_alta(request):
    if request.method == "POST":
        nombre_software = request.POST["software"]
        no_licencia = request.POST["licencia"]
        cuenta_email = request.POST["email"]

        licencia = Licencias(software=nombre_software, licencia=no_licencia, email=cuenta_email)
        licencia.save()
    return render(request, "altas/registro_licencia.html")
    

#Vistas para Laptops