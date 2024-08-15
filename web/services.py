from django.contrib import messages
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

def crear_usuario(request, username:str, first_name:str, email:str, password:str, pass_confirm:str):
    if password != pass_confirm:
        messages.warning(request, 'Las contraseñas no coinciden')
        return False
    # Si llega aquí, es porque el password es igual
    if len(password) > 50:
        messages.warning(request, 'La contraseña supera los 50 caracteres')
        return False
    # Si llega aquí, es porque el password es menos a 50 caracteres
    try:
        user = User.objects.create_user(
            username,
            email,
            password,
            first_name=first_name,
        )
    except IntegrityError:
        messages.warning(request, 'El usuario elegido ya existe')
        return False
    except Exception:
        messages.warning(request, 'No se ha podido registrar el usuario')
        return False
    # Si llega aquí, es porque se creó el usuari
    messages.success(request, '¡Usuario creado con éxito! Por favor, ingrese')
    return True