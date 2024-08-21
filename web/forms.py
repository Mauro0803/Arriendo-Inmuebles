from django import forms
from .models import *

class Crear_ComunaForm(forms.Form):
    comuna = forms.CharField(label='Nombre de la Comuna', max_length=100)


class Crear_UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usu_rut', 'usu_nombre1', 'usu_nombre2', 'usu_apellido1', 'usu_apellido2', 'usu_direccion',
                  'usu_telefono', 'usu_correo', 'fk_tu']
        labels = {
            'usu_rut': 'RUT',
            'usu_nombre1': 'Primer Nombre',
            'usu_nombre2': 'Segundo Nombre',
            'usu_apellido1': 'Primer Apellido',
            'usu_apellido2': 'Segundo Apellido',
            'usu_direccion': 'Dirección',
            'usu_telefono': 'Teléfono',
            'usu_correo': 'Correo Electrónico',
            'fk_tu': 'Tipo de Usuario',
        }
    def __init__(self, *args, **kwargs):
        super(Crear_UsuarioForm, self).__init__(*args, **kwargs)
    # Filtrar para que no aparezca el Administrador
        self.fields['fk_tu'].queryset = Tipo_Usuario.objects.exclude(tu_id=3)
'''Explicación:
__init__(self, *args, **kwargs): Sobrescribimos el método __init__ del formulario para poder modificar el queryset de fk_tu.
self.fields['fk_tu'].queryset = TipoUsuario.objects.exclude(tu_id=3): Filtramos las opciones que se mostrarán en el campo fk_tu, excluyendo el tipo de usuario con tu_id=1, que corresponde al "Administrador".
Este cambio evitará que la opción "Administrador" aparezca en el dropdown cuando el usuario esté creando un nuevo registro.
'''

class Crear_Auth_UserForm(forms.ModelForm):
    class Meta:
        model = Auth_User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

     
class Crear_TipoUsuarioForm(forms.Form):
    tipo_user = forms.CharField(label='Tipo de Usuario', max_length=100)


class Crear_RegionForm(forms.Form):
    region = forms.CharField(label='Nombre de la Region', max_length=100)

    
class Crear_TipoInmuebleForm(forms.Form):
    tipo_inmueble = forms.CharField(label='Tipo de Inmueble', max_length=100)    


class Crear_InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['inm_nombre', 'inm_descripcion', 'inm_m2_construidos', 'inm_m2_totales', 'inm_estacionamientos', 'inm_habitaciones',
                  'inm_banos', 'inm_direccion', 'inm_precio', 'inm_url', 'fk_com', 'fk_reg', 'fk_ti']  
        labels = {
            'inm_nombre': 'Nombre del Inmueble',
            'inm_descripcion': 'Descripción',
            'inm_m2_construidos': 'Metros² Construidos',
            'inm_m2_totales': 'Metros² Totales',
            'inm_estacionamientos': 'Estacionamientos',
            'inm_habitaciones': 'Habitaciones',
            'inm_banos': 'Baños',
            'inm_direccion': 'Dirección',
            'inm_precio': 'Precio',
            'inm_url': 'Imagen del Inmueble',
            'fk_com': 'Comuna',
            'fk_reg': 'Región',
            'fk_ti': 'Tipo de Inmueble',
        }

        
class Modificar_UsuarioForm(forms.Form):
    rut = forms.CharField(max_length=9, label="RUT del usuario")
    campo_a_modificar = forms.ChoiceField(
        choices=[
            ('usu_nombre1', 'Primer Nombre'),
            ('usu_nombre2', 'Segundo Nombre'),
            ('usu_apellido1', 'Primer Apellido '),
            ('usu_apellido2', 'Segundo Apellido'),
            ('usu_direccion', 'Dirección'),
            ('usu_telefono', 'Teléfono'),
            ('usu_correo', 'Correo')
        ], 
        label="Campo a modificar"
    )
    nuevo_valor = forms.CharField(max_length=50, label="Nuevo valor")


class Modificar_InmuebleForm(forms.Form):
    id = forms.CharField(max_length=9, label="ID del Inmueble")
    campo_a_modificar = forms.ChoiceField(
        choices=[
            ('inm_nombre', 'Nombre'),
            ('inm_descripcion', 'Descripcion'),
            ('inm_m2_construidos', 'm2 Construidos'),
            ('inm_m2_totales', 'm2 Totales'),
            ('inm_estacionamientos', 'Estacionamientos'),
            ('inm_habitaciones', 'Habitaciones'),
            ('inm_banos', 'Baños'),
            ('inm_direccion', 'Direccion'),
            ('inm_precio', 'Precio'),
            ('fk_com', 'Comuna'),
            ('fk_reg', 'Region'),
            ('fk_ti', 'Tipo de Inmueble'),
            ('inm_url', 'Imagen del Inmueble'),
        ],
        label="Campo a modificar"
    )
    nuevo_valor = forms.CharField(max_length=50, label="Nuevo valor")


class Borrar_UsuarioForm(forms.Form):
    rut = forms.CharField(max_length=9, label="RUT del usuario a borrar")


class Borrar_InmuebleForm(forms.Form):
    id = forms.CharField(max_length=9, label="Id del inmueble a borrar")


class Asignar_Comuna_A_InmuebleForm(forms.Form):
    id_inmueble = forms.CharField(max_length=9, label="ID del Inmueble")
    id_comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), label="Selecciona una Comuna")
    
    class Meta:
        model = Comuna
        fields = ['com_comuna']

class Asignar_Region_A_InmuebleForm(forms.Form):
    id_inmueble = forms.CharField(max_length=9, label="ID del Inmueble")
    id_region = forms.ModelChoiceField(queryset=Region.objects.all(), label="Selecciona una Region")
    
    class Meta:
        model = Region
        fields = ['reg_region']

class Asignar_Tipo_A_UsuarioForm(forms.Form):
    tipo_usuario = forms.ModelChoiceField(queryset=Tipo_Usuario.objects.all(), label="Selecciona un Tipo de Usuario")
    rut = forms.CharField(max_length=9, label="Rut del Usuario")

    class Meta:
        model = Tipo_Usuario
        fields = ['tu_tipo']

class Asignar_Inmueble_A_UsuarioForm(forms.Form):
    rut = forms.CharField(max_length=9, label="Rut del Usuario")
    id_inmueble = forms.CharField(max_length=9, label="Id del Inmueble")

    class Meta:
        model = Inmueble
        fields = ['inm_id']

class Listado_UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usu_rut', 'usu_nombre1', 'usu_nombre2', 'usu_apellido1', 'usu_apellido2', 'usu_direccion',
                  'usu_telefono', 'usu_correo', 'fk_tu','fk_inm']
        
class Listado_UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usu_rut', 'usu_nombre1', 'usu_nombre2', 'usu_apellido1', 'usu_apellido2', 'usu_direccion',
                  'usu_telefono', 'usu_correo', 'fk_tu','fk_inm']
        
class Listado_InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['inm_id', 'inm_nombre', 'inm_descripcion', 'inm_m2_construidos', 'inm_m2_totales', 'inm_estacionamientos',
                  'inm_habitaciones', 'inm_banos', 'inm_direccion', 'inm_precio', 'fk_com', 'fk_reg', 'fk_ti']
    

