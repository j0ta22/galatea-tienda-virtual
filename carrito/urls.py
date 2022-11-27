from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "carrito"
urlpatterns = [
    path('agregar/<int:articulo_id>/', views.agregar_articulo, name='agregar'),
    path('eliminar/<int:articulo_id>/', views.eliminar_articulo, name='eliminar'),
    path('quitar/<int:articulo_id>/', views.quitar_articulo, name='quitar'),
    path('limpiar/', views.limpiar_carrito, name='limpiar'),
    
]