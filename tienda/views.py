from django.shortcuts import render, HttpResponse

from carrito.carrito import Carrito
#from servicios.models import Servicio
# Create your views here.


def home(request):

    carrito = Carrito(request)

    return render(request, 'tienda/home.html')

"""def servicios(request):

    servicios = Servicio.objects.all()
    print(servicios)
    return render(request, 'tienda/servicios.html', {"servicios" : servicios})"""

"""def tienda(request):

    return render(request, 'tienda/tienda.html')"""

"""def blog(request):

    return render(request, 'tienda/blog.html')"""

"""def contacto(request):

    return render(request, 'tienda/contacto.html')"""
    