from django.contrib import admin
from pedidos.models import Pedido, LineaPedido
# Register your models here.
admin.site.register([Pedido, LineaPedido])