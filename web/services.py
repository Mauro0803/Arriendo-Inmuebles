from web.models import *
from django.contrib.auth.hashers import make_password

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
    
def modificar_usuario(rut, **kwargs): #Ejemplo: modificar_usuario(169358079, usu_nombre2 = 'Esteban')
    mod_usuario = Usuario.objects.get(usu_rut=rut)  # Obtener la instancia del Usuario por el rut

    # Actualizar los campos del usuario según kwargs
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

def borrar_inmueble(id):
    borrar = Inmueble.objects.get(inm_id=id)
    borrar.delete()

def listar_todo():
    usuarios = Usuario.objects.all()
    tipo_usuarios = Tipo_Usuario.objects.all()
    inmuebles = Inmueble.objects.all()
    comunas = Comuna.objects.all()
    regiones = Region.objects.all()
    tipo_inmuebles = Tipo_Inmueble.objects.all()
    
    for usuario in usuarios:
        print(f"•Usuario: {usuario.usu_rut}")
    for tipousuario in tipo_usuarios:
        print(f"•TipoUsuario: {tipousuario.tu_tipo}")
    for inmueble in inmuebles:
        print(f"•Inmueble: {inmueble.inm_nombre}")
    for comuna in comunas:
        print(f"•Comuna: {comuna.com_comuna}")
    for region in regiones:
        print(f"•Region: {region.reg_region}")
    for tipo_inmueble in tipo_inmuebles:
        print(f"•TipoInmueble: {tipo_inmueble.ti_tipo}")




# def crear_comuna(comuna):
#     nueva_comuna = Comuna(com_comuna = comuna)
#     nueva_comuna.save()

# def crear_tipo_usuario(tipo):
#     nuevo_tipo_usuario = Tipo_Usuario(tu_tipo = tipo)
#     nuevo_tipo_usuario.save()

# def crear_region(region):
#     nueva_region = Region(reg_region = region)
#     nueva_region.save()

# def crear_tipo_inmueble(tipo):
#     nuevo_tipo_inmueble = Tipo_Inmueble(ti_tipo = tipo)
#     nuevo_tipo_inmueble.save()


# def asignar_comuna_a_inmueble(id_inmueble, id_comuna):
#     inmueble = Inmueble.objects.get(inm_id=id_inmueble)
#     comuna = Comuna.objects.get(com_comuna = id_comuna)
#     inmueble.fk_com = comuna
#     inmueble.save()


# def asignar_region_a_inmueble(id_inmueble, id_region):
#     inmueble = Inmueble.objects.get(inm_id=id_inmueble)
#     region = Region.objects.get(reg_region = id_region)
#     inmueble.fk_reg = region
#     inmueble.save()   


# def asignar_tipo_a_usuario(tipo_usuario, rut):
#     asignar_usuario = Usuario.objects.get(usu_rut=rut)
#     tipo_usuario = Tipo_Usuario.objects.get(tu_tipo=tipo_usuario)
#     asignar_usuario.fk_tu = tipo_usuario
#     asignar_usuario.save()


# def asignar_inmueble_a_usuario(rut, id_inmueble):
#     usuario = Usuario.objects.get(usu_rut = rut)
#     asignar_inmueble = Inmueble.objects.get(inm_id = id_inmueble)
#     usuario.fk_inm = asignar_inmueble
#     usuario.save()

# def listar_usuarios():
#     lista = Usuario.objects.all()
#     for usuario in lista:
#         print(f"• {usuario.usu_nombre1} {usuario.usu_apellido1}")
