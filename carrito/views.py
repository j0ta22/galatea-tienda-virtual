from django.shortcuts import render, redirect
from .carrito import Carrito
from ecomerce.models import Articulo
# Create your views here.

def agregar_articulo(request, articulo_id):
    carrito = Carrito(request)
    articulo = Articulo.objects.get(id=articulo_id)
    carrito.agregar(articulo=articulo)
    print(articulo)
    return redirect('tienda')

def eliminar_articulo(request, articulo_id):
    carrito = Carrito(request)
    articulo = Articulo.objects.get(id=articulo_id)
    carrito.eliminar(articulo=articulo)

    return redirect('tienda')

def quitar_articulo(request, articulo_id):
    carrito = Carrito(request)
    articulo = Articulo.objects.get(id=articulo_id)
    carrito.quitar_articulo(articulo=articulo)

    return redirect('tienda')

def limpiar_carrito(request, articulo_id):
    carrito = Carrito(request)
    carrito.limpiar_carrito()

    return redirect('tienda')