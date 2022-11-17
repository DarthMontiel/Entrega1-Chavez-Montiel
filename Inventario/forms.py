from django import forms

class LaptopFormulario(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    memoriaRam = forms.IntegerField()
    DiscoDuro = forms.IntegerField()
    DiscoSSD = forms.IntegerField()
    Procesador = forms.CharField()

class MovilFormulario(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    ram = forms.IntegerField()
    memoria = forms.IntegerField()

class licencias(forms.Form):
    software = forms.CharField()
    licencia = forms.CharField()
    email = forms.EmailField()