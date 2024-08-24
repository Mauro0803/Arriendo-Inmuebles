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


class Crear_Auth_UserForm(forms.ModelForm):
    class Meta:
        model = Auth_User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


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
    campo_a_modificar = forms.ChoiceField(
        choices=[
            ('usu_nombre1', 'Primer Nombre'),
            ('usu_nombre2', 'Segundo Nombre'),
            ('usu_apellido1', 'Primer Apellido'),
            ('usu_apellido2', 'Segundo Apellido'),
            ('usu_direccion', 'Dirección'),
            ('usu_telefono', 'Teléfono'),
            ('usu_correo', 'Correo'),
        ], 
        label="Campo a modificar"
    )
    nuevo_valor = forms.CharField(max_length=50, label="Nuevo valor")


class Modificar_InmuebleForm(forms.Form):
    def __init__(self, *args, **kwargs):
        inmuebles = kwargs.pop('inmuebles', None)
        super().__init__(*args, **kwargs)
        
        # Poblamos el campo de selección con los inmuebles del usuario
        self.fields['id'] = forms.ChoiceField(
            choices=[(inmueble.inm_id, inmueble.inm_nombre) for inmueble in inmuebles],
            label="Selecciona el Inmueble"
        )
    
    campo_a_modificar = forms.ChoiceField(
        choices=[
            ('inm_nombre', 'Nombre'),
            ('inm_descripcion', 'Descripción'),
            ('inm_m2_construidos', 'm2 Construidos'),
            ('inm_m2_totales', 'm2 Totales'),
            ('inm_estacionamientos', 'Estacionamientos'),
            ('inm_habitaciones', 'Habitaciones'),
            ('inm_banos', 'Baños'),
            ('inm_direccion', 'Dirección'),
            ('inm_precio', 'Precio'),
            ('fk_com', 'Comuna'),
            ('fk_reg', 'Región'),
            ('fk_ti', 'Tipo de Inmueble'),
            ('inm_url', 'Imagen del Inmueble'),
        ],
        label="Campo a modificar"
    )
    nuevo_valor = forms.CharField(max_length=50, label="Nuevo valor")


class Borrar_UsuarioForm(forms.Form):
    rut = forms.CharField(max_length=9, label="RUT del usuario a borrar")


class Borrar_InmuebleForm(forms.Form):
    def __init__(self, *args, **kwargs):
        inmuebles = kwargs.pop('inmuebles', None)
        super().__init__(*args, **kwargs)
        
        # Poblamos el campo de selección con los inmuebles del usuario
        self.fields['id'] = forms.ChoiceField(
            choices=[(inmueble.inm_id, inmueble.inm_nombre) for inmueble in inmuebles],
            label="Selecciona el Inmueble a Borrar"
        )


class Listado_InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['inm_id', 'inm_nombre', 'inm_descripcion', 'inm_m2_construidos', 'inm_m2_totales', 'inm_estacionamientos',
                  'inm_habitaciones', 'inm_banos', 'inm_direccion', 'inm_precio', 'fk_com', 'fk_reg', 'fk_ti']
        

class Filtro_InmuebleForm(forms.Form):
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), required=False, label='Comuna')
    region = forms.ModelChoiceField(queryset=Region.objects.all(), required=False, label='Región')
    tipo_inmueble = forms.ModelChoiceField(queryset=Tipo_Inmueble.objects.all(), required=False, label='Tipo de Inmueble')
    precio_min = forms.DecimalField(required=False, label='Precio Mínimo', min_value=0)
    precio_max = forms.DecimalField(required=False, label='Precio Máximo', min_value=0)