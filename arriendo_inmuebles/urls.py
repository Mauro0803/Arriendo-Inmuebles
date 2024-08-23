from django.contrib import admin
from django.urls import path, include
from web.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("", index, name='index'),
    path('detalle_inmueble/<int:id>/', detalle_inmueble, name='detalle_inmueble'),
    path('crear_auth_user/', crear_auth_user_view, name='crear_auth_user'),
    path('crear_usuario/<int:auth_user_id>/', crear_usuario_view, name='crear_usuario'),
    path('crear_usuario/', crear_usuario_view, name='crear_usuario'),
    path('crear_inmueble/', crear_inmueble_view, name='crear_inmueble'),
    path('modificar_usuario/', modificar_usuario_view, name='modificar_usuario'),
    path('modificar_inmueble/', modificar_inmueble_view, name='modificar_inmueble'),
    path('borrar_usuario/', borrar_usuario_view, name='borrar_usuario'),
    path('borrar_inmueble/', borrar_inmueble_view, name='borrar_inmueble'),
    path('listado_inmueble/', listado_inmueble_view, name='listado_inmueble'),
    path('perfil_usuario/', perfil_usuario_view, name='perfil_usuario'),
]
