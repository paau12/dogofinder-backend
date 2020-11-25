from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path(
        'mascotas/<int:id>',
        views.get_delete_update_mascota,
        name='get_delete_update_mascota'
    ),
    path(
        'mascotas/',
        views.get_post_mascotas,
        name='get_post_mascotas'
    ),
    path(
        'mascota_perdida/<int:id>/',
        views.GPD_mascota_perdida,
        name='GPD_mascota_perdida'
    ),
    path(
        'mascota_perdida/',
        views.post_mascota_perdida,
        name='post_mascota_perdida'
    ),
    path(
        'mascota_encontrada/<int:id>/',
        views.GPD_mascota_encontrada,
        name='GPD_mascota_encontrada'
    ),
    path(
        'mascota_encontrada/',
        views.post_mascota_encontrada,
        name='post_mascota_encontrada'
    ),
    path(
        'usuario/<int:id>/',
        views.GPD_usuario,
        name='GPD_usuario'
    ),
    # path(
    #     'registro/',
    #     views.crear_usuario,
    #     name='crear_usuario'
    # ),
    # path(
    #     'login/',
    #     obtain_auth_token,
    #     name='login'
    # ),
    path(
        'usuario/',
        views.post_usuario,
        name='post_usuario'
    ),
    path(
        'reporte/<int:id>/',
        views.GPD_reporte,
        name='GPD_reporte'
    ),
    path(
        'reporte/',
        views.post_reporte,
        name='post_reporte'
    ),
    path(
        'reporte/<int:id>/',
        views.GPD_reporte,
        name='GPD_reporte'
    ),
    path(
        'reporte_avistado/',
        views.post_reporte_avistado,
        name='GPD_reporte_avistado'
    ),
    path(
        'reporte_encontrado/',
        views.post_reporte_encontrado,
        name='GPD_reporte_encontrado'
    ),
    path(
        'reporte_perdido/',
        views.post_reporte_perdido,
        name='GPD_reporte_perdido'
    ),
]
