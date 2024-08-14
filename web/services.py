from web.models import *

def crear_usuario(Rut, Nombre1, Nombre2, Apellido1, Apellido2, Direccion, Telefono, Correo):
    nuevo_usuario = Usuario(usu_rut = Rut, usu_nombre1 = Nombre1, usu_nombre2 = Nombre2, usu_apellido1 = Apellido1,
                            usu_apellido2= Apellido2, usu_direccion= Direccion, usu_telefono= Telefono, usu_correo= Correo)
    nuevo_usuario.save()

def crear_tipo_usuario(tipo):
    nuevo_tipo_usuario = Tipo_Usuario(tu_tipo = tipo)
    nuevo_tipo_usuario.save()

def asignar_tipo_a_usuario(tipo_usuario, rut):
    asignar_usuario = Usuario.objects.get(usu_rut=rut)
    tipo_usuario = Tipo_Usuario.objects.get(tu_tipo=tipo_usuario)
    asignar_usuario.fk_tu = tipo_usuario
    asignar_usuario.save()

def modificar_usuario(rut, **kwargs): #Ejemplo: modificar_usuario(169358079, usu_nombre2 = 'Esteban')
    mod_usuario = Usuario.objects.get(usu_rut=rut)  # Obtener la instancia del Usuario por el rut

    # Actualizar los campos del usuario según kwargs
    for campo, valor in kwargs.items():
        if hasattr(mod_usuario, campo):
            setattr(mod_usuario, campo, valor)
    mod_usuario.save()

def listar_usuarios():
    lista = Usuario.objects.all()
    for usuario in lista:
        print(f"• {usuario.usu_nombre1} {usuario.usu_apellido1}")

def borrar_usuario(rut):
    borrar = Usuario.objects.get(usu_rut=rut)  # Obtener la instancia del Usuario por el rut
    borrar.delete()

################################ INMUEBLE #########################################################################

def crear_comuna(comuna):
    nueva_comuna = Comuna(com_comuna = comuna)
    nueva_comuna.save()

def crear_region(region):
    nueva_region = Region(reg_region = region)
    nueva_region.save()

def crear_tipo_inmueble(tipo):
    nuevo_tipo_inmueble = Tipo_Inmueble(ti_tipo = tipo)
    nuevo_tipo_inmueble.save()

def crear_inmueble(nombre, descripcion, m2_construidos, m2_totales, estacionamientos, habitaciones,
                   banos, direccion, precio):
    nuevo_inmueble = Inmueble(inm_nombre = nombre, inm_descripcion = descripcion, inm_m2_construidos = m2_construidos, 
                              inm_m2_totales = m2_totales, inm_estacionamientos = estacionamientos, inm_habitaciones = habitaciones,
                              inm_banos = banos, inm_direccion = direccion, inm_precio = precio)
    nuevo_inmueble.save()

def asignar_comuna(id_inmueble, id_comuna):
    inmueble = Inmueble.objects.get(inm_id=id_inmueble)
    comuna = Comuna.objects.get(com_id = id_comuna)
    inmueble.fk_com = comuna
    inmueble.save()

def asignar_region(id_inmueble, id_region):
    inmueble = Inmueble.objects.get(inm_id=id_inmueble)
    region = Region.objects.get(reg_id = id_region)
    inmueble.fk_reg = region
    inmueble.save()    

#########################################################################################################

def inmueble_asignado_a_usuario(rut, id_inmueble):
    usuario = Usuario.objects.get(usu_rut = rut)
    inmueble = Inmueble.objects.get(inm_id = id_inmueble)
    usuario.fk_inm = inmueble
    usuario.save()

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