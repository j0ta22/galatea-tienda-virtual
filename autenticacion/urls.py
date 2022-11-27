from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Registro, cerrar_sesion, iniciar_sesion


urlpatterns = [
    path('', Registro.as_view(), name= 'registro'),
    path('cerrar_sesion', cerrar_sesion, name= 'logout'),
    path('iniciar_sesion', iniciar_sesion, name= 'login'),
    
]