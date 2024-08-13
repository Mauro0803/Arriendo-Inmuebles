from web.models import *

def crear_usuario(nuevoRut, nuevoNombre1, nuevoNombre2, nuevoApellido1, nuevoApellido2, nuevoDireccion, nuevoTelefono, nuevoCorreo):
    nuevo_usuario = Usuario(rut = nuevoRut, nombre1 = nuevoNombre1, nombre2 = nuevoNombre2, apellido1 = nuevoApellido1,
                            apellido2= nuevoApellido2, direccion= nuevoDireccion, telefono= nuevoTelefono, correo= nuevoCorreo)
    nuevo_usuario.save()

def crear_tipo_usuario(nuevoTipo):
    nuevo_tipo_usuario = TipoUsuario(tipo = nuevoTipo)
    nuevo_tipo_usuario.save()

def asignar_tipo(tipo_usuario_str, rut_usuario):
    usuario = Usuario.objects.get(rut=rut_usuario)
    tipo_usuario = TipoUsuario.objects.get(tipo=tipo_usuario_str)
    usuario.tipo_usuario = tipo_usuario
    usuario.save()

def modificar_usuario(rut_usuario, **kwargs):
    usuario = Usuario.objects.get(rut=rut_usuario)  # Obtener la instancia del Usuario por el rut

    # Actualizar los campos del usuario según kwargs
    for campo, valor in kwargs.items():
        if hasattr(usuario, campo):
            setattr(usuario, campo, valor)
    usuario.save()

def listar_usuarios():
    usuarios = Usuario.objects.all()
    for usuario in usuarios:
        print(f"• {usuario.nombre1}")

def borrar_usuario(rut_usuario):
    usuario = Usuario.objects.get(rut=rut_usuario)  # Obtener la instancia del Usuario por el rut
    usuario.delete()