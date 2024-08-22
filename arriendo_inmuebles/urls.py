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

    # path('asignar_comuna_a_inmueble/', asignar_comuna_a_inmueble_view, name='asignar_comuna_a_inmueble'),
    # path('asignar_region_a_inmueble/', asignar_region_a_inmueble_view, name='asignar_region_a_inmueble'),
    # path('asignar_tipo_a_usuario/', asignar_tipo_a_usuario_view, name='asignar_tipo_a_usuario'),
    # path('asignar_inmueble_a_usuario/', asignar_inmueble_a_usuario_view, name='asignar_inmueble_a_usuario'),
    #path('crear_comuna/', crear_comuna_view, name='crear_comuna'),
    #path('crear_tipo_usuario/', crear_tipo_usuario_view, name='crear_tipo_usuario'),
    #path('crear_region/', crear_region_view, name='crear_region'),
    #path('crear_tipo_inmueble/', crear_tipo_inmueble_view, name='crear_tipo_inmueble'),
    #path('listado_usuario/', listado_usuario_view, name='listado_usuario'),
]
