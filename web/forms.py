from django import forms
from .models import *

class Crear_ComunaForm(forms.Form):
    comuna = forms.CharField(label='Nombre de la Comuna', max_length=100)


class Crear_UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usu_rut', 'usu_nombre1', 'usu_nombre2', 'usu_apellido1', 'usu_apellido2', 'usu_direccion',
                  'usu_telefono', 'usu_correo']

     
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
                  'inm_banos', 'inm_direccion', 'inm_precio']  


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