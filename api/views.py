from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Mascota
from .serializers import MascotaSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_mascota(request, pk):
    try:
        mascota = Mascota.objects.get(pk=pk)

    except Mascota.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Obtener detalles de una mascota
    if request.method == 'GET':
        return Response({})

    # Eliminar una mascota
    elif request.method == 'DELETE':
        return Response({})

    # Actualizar detalles de una mascota
    elif request.method == 'PUT':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_mascotas(request):
    # Obtener todas las mascotas
    if request.method == 'GET':
        return Response({})

    # Insertar un nuevo registro de mascota
    elif request.method == 'POST':
        return Response({})
