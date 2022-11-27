from pdb import post_mortem
from django.shortcuts import redirect, render
from django.core.mail import send_mail, EmailMessage
from .forms import Contacto

# Create your views here.

def contacto(request):

    formulario = Contacto()

    if request.method == "POST":
        formulario = Contacto(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            correo = EmailMessage("Correo de contacto desde Galatea", "Usuario: {}, Email: {}.\n\nMensaje:\n{}".format(nombre, email, contenido), 
            "", ['juanpcandal@gmail.com'], ['juanpcandal@gmail.com'], reply_to=[email])

            try:
                correo.send()
                return redirect("/contacto/?Valido")
            except:
                return redirect("/contacto/?Invalido")

    return render(request, 'contacto/contacto.html', {'formulario' : formulario})


"""def contacto(request):
    if request.method == 'POST':

        formulario = FormularioContacto(request.POST)

        if formulario.is_valid():
            info_form = formulario.cleaned_data
            
            send_mail(info_form['asunto'], info_form['mensaje'], 
            info_form.get('email', 'juanpcandal@gmail.com'), ['juanpcandal@gmail.com'],)

            return render(request, 'gracias.html')

    else:
        formulario = FormularioContacto()

    return render(request, 'formulario_contacto.html', {"form" : formulario})"""

