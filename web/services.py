from web.models import *
from django.contrib.auth.hashers import make_password
from django.core.exceptions import PermissionDenied

#kwargs: Es un diccionario que contiene todos los campos del formulario. Al usar **kwargs, la función puede recibir todos
#        los argumentos de palabra clave y pasarlos directamente al constructor de Usuario.
def crear_usuario(**kwargs):
    nuevo_usuario = Usuario(**kwargs)
    nuevo_usuario.save()

def crear_auth_user(**kwargs):
    password = kwargs.get('password')
    if password:
        # Encriptar la contraseña
        kwargs['password'] = make_password(password)
    
    nuevo_usuario = Auth_User(**kwargs)
    nuevo_usuario.save()
    return nuevo_usuario

def crear_inmueble(**kwargs):
    nuevo_inmueble = Inmueble(**kwargs)
    nuevo_inmueble.save()
    
def modificar_usuario(rut, **kwargs):
    mod_usuario = Usuario.objects.get(usu_rut=rut)  # Obtén la instancia del Usuario por el rut

    # Actualiza los campos del usuario según kwargs
    for campo, valor in kwargs.items():
        if hasattr(mod_usuario, campo):
            setattr(mod_usuario, campo, valor)
    mod_usuario.save()

def modificar_inmueble(id, **kwargs):
    mod_inmueble = Inmueble.objects.get(inm_id=id)

    for campo, valor in kwargs.items():
        if hasattr(mod_inmueble, campo):
            setattr(mod_inmueble, campo, valor)
    mod_inmueble.save()

def borrar_usuario(rut):
    borrar = Usuario.objects.get(usu_rut=rut)  # Obtener la instancia del Usuario por el rut
    borrar.delete()

def borrar_inmueble(id, inmuebles_usuario):
    # Intentar obtener el inmueble del usuario
    try:
        inmueble = inmuebles_usuario.get(inm_id=id)
        inmueble.delete()  # Si el inmueble pertenece al usuario, se borra
    except Inmueble.DoesNotExist:
        raise PermissionDenied("No tienes permiso para borrar este inmueble.")

def obtener_usuario_por_auth_user(auth_user_id):
    return Usuario.objects.filter(fk_au=auth_user_id).select_related('fk_tu').first()

def obtener_usuario(request):
    return Usuario.objects.get(fk_au=request.user.id)

def obtener_inmuebles_por_usuario(usuario_rut):
    return Inmueble.objects.filter(fk_usu_usu_rut=usuario_rut)

def obtener_inmueble_por_id(id):
    return Inmueble.objects.get(inm_id=id)

def obtener_inmuebles():
    return Inmueble.objects.all()

def obtener_comunas():
    return Comuna.objects.all()

def obtener_regiones():
    return Region.objects.all()

def obtener_tipo_inmuebles():
    return Tipo_Inmueble.objects.all()