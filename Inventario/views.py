from django.shortcuts import render
from django.http import HttpResponse
from Inventario.forms import *
from Inventario.models import *

# Create your views here.
#Vista para la página de inicio
def inicio(request):
    return render(request, "Inventario/index.html")



#Vista para las laptops
def formulario_laptop(request):
    pass

#=========================================================
def alta_laptop(request):
    if request.method == "POST":
        #Creamos el formulario
        formulario_alta_laptop = LaptopFormulario(request.POST)
        if formulario_alta_laptop.is_valid():
            data = formulario_alta_laptop.cleaned_data
            laptop = laptops(marca=data["marca"], modelo=data["modelo"], memoriaRam=data["memoriaRam"], DiscoDuro=data["DiscoDuro"], Procesador=data["Procesador"])
            laptop.save()
            return render(request, "Inventario/alta_laptop.html")
    else:
        formulario_alta_laptop = LaptopFormulario()
    
    contexto = {'formulario_alta_laptop',formulario_alta_laptop}
    return render (request, "Inventario/index.html/", contexto)

#==================================================================
def busqueda_laptop(request):
    return render(request, "Inventario/busqueda_laptop.html")

def busqueda_laptop_resultado(request):
    return render(request, "Inventario/busqueda_laptop_resultado.html")



#Vista para los dispositivos moviles
def alta_movil(request):
    return render(request, "Inventario/alta_movil.html")

def busqueda_movil(request):
    return render(request, "Inventario/busqueda_movil.html")

def busqueda_movil_resulado(request):
    return render(request, "Inventario/busqueda_movil_resultado.html")



#Vistas para las licencias
def alta_licencia(request):
    return render(request, "Inventario/busqueda_movil_resultado.html")

def busqueda_licencia(request):
    return render(request, "Inventario/busqueda_movil_resultado.html")

def busqueda_licencia_resulado(request):
    return render(request, "Inventario/busqueda_movil_resultado.html")
