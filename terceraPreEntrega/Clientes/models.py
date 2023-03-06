from django.db import models

# Create your models here.

class Cliente(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.EmailField()

class Vendedor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    puestoDeTrabajo = models.CharField(max_length=40)
    

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()