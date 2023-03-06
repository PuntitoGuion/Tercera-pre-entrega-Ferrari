from django.urls import path
from Clientes import views

urlpatterns = [
    path('',views.inicio, name='Inicio'),
    path('cliente',views.cliente, name='Cliente'),
    path('producto',views.producto, name='Producto'),
    path('vendedor',views.vendedor, name='Vendedor'),
    path('buscarProducto',views.buscarProducto, name='BuscarProducto'),
    path('exito',views.exito, name='exito'),
    path('buscar/',views.buscar),
]