from django.http import HttpResponse
from django.shortcuts import render
from Clientes.models import Cliente,Vendedor,Producto
from Clientes.forms import ClienteFormulario,ProductoFormulario,VendedorFormulario

# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def exito(request):
    return render(request,'exito.html')

def cliente(request):
    if request.method == "POST":
        miFormulario = ClienteFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            #print(informacion)
            cliente = Cliente(nombre=informacion['nombre'],
                            apellido=informacion['apellido'],
                            edad=informacion['edad'],
                            email=informacion['email'])
            cliente.save()
            return render(request,'exito.html')

    else:
        miFormulario = ClienteFormulario()

    return render(request, 'cliente.html',{"miFormulario":miFormulario})


def vendedor(request):
    if request.method == "POST":
        miFormulario = VendedorFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            producto = Vendedor(nombre=informacion['nombre'],
                            precio=informacion['apellido'],
                            puestoDeTrabajo=informacion['puestoDeTrabajo'])

            producto.save()
            return render(request,'exito.html')

    else:
        miFormulario = VendedorFormulario()

    return render(request, 'vendedor.html',{"miFormulario":miFormulario})

def producto(request):
    if request.method == "POST":
        miFormulario = ProductoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            producto = Producto(nombre=informacion['nombre'],
                            precio=informacion['precio'])

            producto.save()
            return render(request,'exito.html')

    else:
        miFormulario = ProductoFormulario()

    return render(request, 'producto.html',{"miFormulario":miFormulario})


def buscarProducto(request):

    return render(request, 'buscarProducto.html')

def buscar(request):
    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        productos = Producto.objects.filter(nombre__icontains=nombre)

        return render(request,'resultado.html',{'productos':productos})

    else:
        respuesta = 'No enviaste datos'
    

    return HttpResponse(respuesta)