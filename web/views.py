from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .services import *
from .forms import *

@login_required
def index(request):
    usuario = Usuario.objects.filter(fk_au=request.user.id).select_related('fk_tu').first() # request.user representa al usuario actualmente autenticado,
    inmueble = Inmueble.objects.all()                                                       # y .id es su ID único en la base de datos. Este ID es el valor 
                                                                                            # que se usa para comparar con el campo fk_au de la tabla Usuario.
    return render(request, 'index.html', {'usuario': usuario, 'inmueble': inmueble })       # Usamos select_related para traer la relación con TipoUsuario


def crear_usuario_view(request, auth_user_id):
    if request.method == 'POST':
        form = Crear_UsuarioForm(request.POST)
        if form.is_valid():
            nuevo_usuario = form.save(commit=False)
            nuevo_usuario.fk_au_id = auth_user_id  # Asignar el ID del Auth_User
            nuevo_usuario.save()
            return redirect('index')  # Redirigir a una página de éxito o inicio
    else:
        form = Crear_UsuarioForm()
    
    return render(request, 'crear_usuario.html', {'form': form})


def crear_auth_user_view(request):
    if request.method == 'POST':
        form = Crear_Auth_UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            nuevo_usuario_auth = crear_auth_user(**data)
            # Redirigir a la vista de creación de Usuario, pasando el ID del nuevo Auth_User
            return redirect(reverse('crear_usuario', kwargs={'auth_user_id': nuevo_usuario_auth.id}))
    else:
        form = Crear_Auth_UserForm()
    
    return render(request, 'crear_auth_user.html', {'form': form})


def crear_inmueble_view(request):
    usuario = Usuario.objects.filter(fk_au=request.user.id).select_related('fk_tu').first()
    if request.method == 'POST':
        form = Crear_InmuebleForm(request.POST)
        if form.is_valid():
            crear_inmueble(**form.cleaned_data)
            return redirect('/')
    else:
        form = Crear_InmuebleForm()
    return render(request, 'crear_inmueble.html', {'usuario': usuario, 'form': form})

def modificar_usuario_view(request):
    if request.method == 'POST':
        form = Modificar_UsuarioForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            campo_a_modificar = form.cleaned_data['campo_a_modificar']
            nuevo_valor = form.cleaned_data['nuevo_valor']
            modificar_usuario(rut, **{campo_a_modificar: nuevo_valor})
            return redirect('/')
    else:
        form = Modificar_UsuarioForm()
    return render(request, 'modificar_usuario.html', {'form': form})

def modificar_inmueble_view(request):
    usuario = Usuario.objects.filter(fk_au=request.user.id).select_related('fk_tu').first()
    if request.method == 'POST':
        form = Modificar_InmuebleForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            campo_a_modificar = form.cleaned_data['campo_a_modificar']
            nuevo_valor = form.cleaned_data['nuevo_valor']
            modificar_inmueble(id, **{campo_a_modificar: nuevo_valor})
            return redirect('/')
    else:
        form = Modificar_InmuebleForm()
    return render(request, 'modificar_inmueble.html', {'usuario': usuario, 'form': form})

def borrar_usuario_view(request):
    if request.method == 'POST':
        form = Borrar_UsuarioForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            borrar_usuario(rut)
            return redirect('/')
    else:
        form = Borrar_UsuarioForm()
    return render(request, 'borrar_usuario.html', {'form': form})

def borrar_inmueble_view(request):
    usuario = Usuario.objects.filter(fk_au=request.user.id).select_related('fk_tu').first()
    if request.method == 'POST':
        form = Borrar_InmuebleForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            borrar_inmueble(id)
            return redirect('/')
    else:
        form = Borrar_InmuebleForm()
    return render(request, 'borrar_inmueble.html', {'usuario': usuario, 'form': form})


def asignar_comuna_a_inmueble_view(request):
    if request.method =='POST':
        form = Asignar_Comuna_A_InmuebleForm(request.POST)
        if form.is_valid():
            id_inmueble = form.cleaned_data['id_inmueble']
            id_comuna = form.cleaned_data['id_comuna']
            asignar_comuna_a_inmueble(id_inmueble, id_comuna)
            return redirect('/')

        else:
            messages.error(request, "Your data has not been saved!")
            return HttpResponseRedirect('/')
    else:
        form = Asignar_Comuna_A_InmuebleForm()
        return render(request, 'asignar_comuna_a_inmueble.html', {'form': form})
    

def asignar_region_a_inmueble_view(request):
    if request.method =='POST':
        form = Asignar_Region_A_InmuebleForm(request.POST)
        if form.is_valid():
            id_inmueble = form.cleaned_data['id_inmueble']
            id_region = form.cleaned_data['id_region']
            asignar_region_a_inmueble(id_inmueble, id_region)
            return redirect('/')

        else:
            messages.error(request, "Your data has not been saved!")
            return HttpResponseRedirect('/')
    else:
        form = Asignar_Region_A_InmuebleForm()
        return render(request, 'asignar_region_a_inmueble.html', {'form': form})
    

def asignar_tipo_a_usuario_view(request):
    if request.method =='POST':
        form = Asignar_Tipo_A_UsuarioForm(request.POST)
        if form.is_valid():
            tipo_usuario = form.cleaned_data['tipo_usuario']
            rut = form.cleaned_data['rut']

            asignar_tipo_a_usuario(tipo_usuario, rut)
            return redirect('/')

        else:
            messages.error(request, "Your data has not been saved!")
            return HttpResponseRedirect('/')
    else:
        form = Asignar_Tipo_A_UsuarioForm()
        return render(request, 'asignar_tipo_a_usuario.html', {'form': form})
    

def asignar_inmueble_a_usuario_view(request):
    if request.method =='POST':
        form = Asignar_Inmueble_A_UsuarioForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            id_inmueble = form.cleaned_data['id_inmueble']


            asignar_inmueble_a_usuario(rut, id_inmueble)
            return redirect('/')

        else:
            messages.error(request, "Your data has not been saved!")
            return HttpResponseRedirect('/')
    else:
        form = Asignar_Inmueble_A_UsuarioForm()
        return render(request, 'asignar_inmueble_a_usuario.html', {'form': form})

def listado_usuario_view(request):
    usuario = Usuario.objects.all()           
    return render(request, 'listado_usuario.html', {'usuario': usuario})

def listado_inmueble_view(request):
    usuario = Usuario.objects.filter(fk_au=request.user.id).select_related('fk_tu').first()
    inmueble = Inmueble.objects.all()           
    return render(request, 'listado_inmueble.html', {'usuario': usuario, 'inmueble': inmueble})  

def index_arrendatario_view(request):
    return render(request, 'index_arrendatario.html', {})

def index_arrendador_view(request):
    return render(request, 'index_arrendador.html', {})

def detalle_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, pk=id)
    return render(request, 'detalle_inmueble.html', {'inmueble': inmueble})


def crear_comuna_view(request):
    if request.method == 'POST':
        form = Crear_ComunaForm(request.POST)
        if form.is_valid():
            crear_comuna(form.cleaned_data['comuna'])
            return redirect('/')
    else:
        form = Crear_ComunaForm()
    return render(request, 'crear_comuna.html', {'form': form})

def crear_tipo_usuario_view(request):
    if request.method == 'POST':
        form = Crear_TipoUsuarioForm(request.POST)
        if form.is_valid():
            crear_tipo_usuario(form.cleaned_data['tipo_user'])
            return redirect('/')
    else:
        form = Crear_TipoUsuarioForm()
    return render(request, 'crear_tipo_usuario.html', {'form': form})

def crear_region_view(request):
    if request.method == 'POST':
        form = Crear_RegionForm(request.POST)
        if form.is_valid():
            crear_region(form.cleaned_data['region'])
            return redirect('/')
    else:
        form = Crear_RegionForm()
    return render(request, 'crear_region.html', {'form': form})

def crear_tipo_inmueble_view(request):
    if request.method == 'POST':
        form = Crear_TipoInmuebleForm(request.POST)
        if form.is_valid():
            crear_tipo_inmueble(form.cleaned_data['tipo_inmueble'])
            return redirect('/')
    else:
        form = Crear_TipoInmuebleForm()
    return render(request, 'crear_tipo_inmueble.html', {'form': form})
