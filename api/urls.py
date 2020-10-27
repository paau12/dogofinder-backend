from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^api/v1/mascotas/(?P<pk>[0-9]+)$',
        views.get_delete_update_mascota,
        name='get_delete_update_mascota'
    ),
    url(
        r'^api/v1/mascotas/$',
        views.get_post_mascotas,
        name='get_post_mascotas'
    )
]
