from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .services import *
from .forms import *

@login_required
def index(request):
    usuario = obtener_usuario_por_auth_user(request.user.id)
    inmueble = obtener_inmuebles()
    return render(request, 'index.html', {'usuario': usuario, 'inmueble': inmueble})   


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


@login_required
def crear_usuario_view(request, auth_user_id):
    if request.method == 'POST':
        form = Crear_UsuarioForm(request.POST)
        if form.is_valid():
            nuevo_usuario = form.save(commit=False)
            nuevo_usuario.fk_au_id = auth_user_id  # Asignar el ID del Auth_User
            nuevo_usuario.save()
            return redirect('index')  
    else:
        form = Crear_UsuarioForm()
    
    return render(request, 'crear_usuario.html', {'form': form})


@login_required
def crear_inmueble_view(request):
    usuario = obtener_usuario_por_auth_user(request.user.id)
    user = obtener_usuario(request)  # Obtiene el usuario autenticado VERIFICAR

    if request.method == 'POST':
        form = Crear_InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.fk_usu_usu_rut = user  # Asigna el usuario al inmueble
            inmueble.save()
            return redirect('/')
    else:
        form = Crear_InmuebleForm()
    
    return render(request, 'crear_inmueble.html', {'usuario': usuario, 'form': form})


@login_required
def modificar_usuario_view(request):
    usuario = obtener_usuario_por_auth_user(request.user.id)  # Obtén el usuario autenticado
    
    if request.method == 'POST':
        form = Modificar_UsuarioForm(request.POST)
        if form.is_valid():
            campo_a_modificar = form.cleaned_data['campo_a_modificar']
            nuevo_valor = form.cleaned_data['nuevo_valor']
            modificar_usuario(usuario.usu_rut, **{campo_a_modificar: nuevo_valor})  # Modifica los datos del usuario autenticado
            return redirect('/')
    else:
        form = Modificar_UsuarioForm()
    
    return render(request, 'modificar_usuario.html', {'usuario': usuario, 'form': form})


@login_required
def modificar_inmueble_view(request):
    usuario = obtener_usuario_por_auth_user(request.user.id)
    inmuebles_usuario = obtener_inmuebles_por_usuario(usuario.usu_rut)
    
    if request.method == 'POST':
        form = Modificar_InmuebleForm(request.POST, inmuebles=inmuebles_usuario)
        if form.is_valid():
            id = form.cleaned_data['id']
            campo_a_modificar = form.cleaned_data['campo_a_modificar']
            nuevo_valor = form.cleaned_data['nuevo_valor']
            modificar_inmueble(id, **{campo_a_modificar: nuevo_valor})
            return redirect('/')
    else:
        form = Modificar_InmuebleForm(inmuebles=inmuebles_usuario)
    
    return render(request, 'modificar_inmueble.html', {'usuario': usuario, 'form': form})


@login_required
def borrar_usuario_view(request):
    usuario = obtener_usuario_por_auth_user(request.user.id)
    if request.method == 'POST':
        form = Borrar_UsuarioForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            borrar_usuario(rut)
            return redirect('/')
    else:
        form = Borrar_UsuarioForm()
    return render(request, 'borrar_usuario.html', {'usuario': usuario,'form': form})


@login_required
def borrar_inmueble_view(request):
    # Obtener el usuario autenticado
    usuario = obtener_usuario_por_auth_user(request.user.id)

    # Filtrar los inmuebles que pertenecen al usuario
    inmuebles_usuario = obtener_inmuebles_por_usuario(usuario.usu_rut)

    if request.method == 'POST':
        form = Borrar_InmuebleForm(request.POST, inmuebles=inmuebles_usuario)
        if form.is_valid():
            id = form.cleaned_data['id']
            borrar_inmueble(id, inmuebles_usuario)  # Pasar los inmuebles del usuario para la validación
            return redirect('/')
    else:
        form = Borrar_InmuebleForm(inmuebles=inmuebles_usuario)
    
    return render(request, 'borrar_inmueble.html', {'usuario': usuario, 'form': form})


@login_required
def listado_inmueble_view(request):
    usuario = obtener_usuario_por_auth_user(request.user.id)
    inmueble = obtener_inmuebles()      
    return render(request, 'listado_inmueble.html', {'usuario': usuario, 'inmueble': inmueble}) 


def detalle_inmueble(request, id):
    usuario = obtener_usuario_por_auth_user(request.user.id)
    inmueble = obtener_inmueble_por_id(id)
    return render(request, 'detalle_inmueble.html', {'usuario': usuario,'inmueble': inmueble})

@login_required
def perfil_usuario_view(request):
    usuario = obtener_usuario(request)
    return render(request, 'perfil_usuario.html', {'usuario': usuario})