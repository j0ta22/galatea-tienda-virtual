from email import message
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Pedido, LineaPedido
from carrito.carrito import Carrito
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.

@login_required(login_url='/autenticacion/login')
def procesar_pedido(request):

    pedido = Pedido.objects.create(user=request.user)
    carrito = Carrito(request)
    lineas_pedido = list()

    for key, value in carrito.carrito.items():
        lineas_pedido.append(LineaPedido(
            producto_id = key,
            cantidad = value['cantidad'],
            user = request.user,
            pedido = pedido
        ))

    LineaPedido.objects.bulk_create(lineas_pedido)

    mail_compra(
        pedido = pedido,
        lineas_pedido = lineas_pedido,
        nombre_usuario = request.user.username,
        mail_usuario = request.user.email
    )

    messages.success(request, 'El pedido ha sido procesado')

    return redirect('../tienda')

def mail_compra(**kwargs):
    asunto = 'Gracias por su compra'
    mensaje = render_to_string('emails/pedido.html',{
        'pedidos' : kwargs.get('pedido'),
        'lineas_pedido' : kwargs.get('lineas_pedido'),
        'nombre_usuario' : kwargs.get('nombres_usuario')
    })
    mensaje_cuerpo = strip_tags(mensaje)
    from_mail = 'juanpcandal@gmail.com'
    #to = kwargs.get('mail_usuario')
    to = 'rociopansechi@gmail.com'
    send_mail(
        asunto,
        mensaje_cuerpo,
        from_mail,
        [to],
        html_message=mensaje
    )

