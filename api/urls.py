from django.urls import path
from . import views


urlpatterns = [
    path(
        'api/v1/mascotas/<int:id>',
        views.get_delete_update_mascota,
        name='get_delete_update_mascota'
    ),
    path(
        'api/v1/mascotas/',
        views.get_post_mascotas,
        name='get_post_mascotas'
    ),
    path(
        'api/v1/usuario/<int:id>',
        views.GPD_usuario,
        name='GPD_usuario'
    ),
    path(
        'api/v1/usuario/',
        views.post_usuario,
        name='post_usuario'
    ),
]
