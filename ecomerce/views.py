from django.shortcuts import render
from .models import Articulo

# Create your views here.
def tienda(request):
    articulos=Articulo.objects.all()
    return render(request, 'ecomerce/tienda.html', {'articulos' : articulos})