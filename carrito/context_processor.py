#from .carrito import Carrito

def importe_total_carrito(request):
    #carrito = Carrito(request)
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session['carrito'].items():
            total = total + float(value['precio'])
    else:
        total = 'Es necesario hacer login'

    return {"importe_total_carrito" : total}
