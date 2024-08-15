from django.shortcuts import render, redirect
from web.models import Flan, Contact
from web.forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.views import View
from web.services import crear_usuario

# Create your views here.
def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        'flanes': flanes_publicos
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        'flanes': flanes_privados
    }
    return render(request, 'welcome.html', context)


def contact(request):
    if request.method == 'GET':
        form = ContactForm()                    # Se crea una instancia del formulario ContactForm sin datos iniciales.
        context = {'form': form}                # Se crea un contexto que contiene el formulario vacío.
        return render(request, 'contact.html', context) # Se renderiza la plantilla 'contact.html' con el contexto.
    else:
        form = ContactForm(request.POST)        # Se crea una instancia de ContactForm con los datos enviados en la solicitud POST.
        if form.is_valid():                     # Se verifica si los datos del formulario son válidos.
            Contact.objects.create(
                **form.cleaned_data
            )                                   # Esta es la forma de pedirle a un modelo que cree un registro usando los datos de un formulario
            return redirect('success')         # Si el formulario es válido, se redirige al usuario a la URL '/success'.
        context = {'form': form}                # Se crea un contexto que contiene el formulario con los datos (válidos o no).
        return render(request, 'contact.html', context) # Se vuelve a renderizar la plantilla con el contexto actualizado.

def success(request):
    return render(request, 'success.html')


class RegisterView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        username = request.POST['username']
        first_name = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password']
        pass_confirm = request.POST['password_repeat']
        crear = crear_usuario(request, username, first_name, email, password, pass_confirm)
        if crear:
            return redirect('login')
        # Si hay errores, mantiene los datos ingresados en el formulario
        return render(request, 'registration/register.html', {
            'username': username,
            'first_name': first_name,
            'email': email,
        })

    def get(self, request):
        return render(request, 'registration/register.html')