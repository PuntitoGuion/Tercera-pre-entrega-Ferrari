
from django import forms


class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    email = forms.EmailField()

class VendedorFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    puestoDeTrabajo = forms.CharField(max_length=40)
    
class ProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    precio = forms.IntegerField()
