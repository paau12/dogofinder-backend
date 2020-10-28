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
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)

    # Insertar un nuevo registro de mascota
    if request.method == 'POST':
        data = {
            'nombre_mascota': request.data.get('nombre_mascota'),
            'tipo_mascota': request.data.get('tipo_mascota'),
            'raza_mascota': request.data.get('raza_mascota'),
            'descripcion_mascota': request.data.get('descripcion_mascota'),
            'codigo_qr': request.data.get('codigo_qr'),
            'in_home': bool(request.data.get('in_home')),
            'id_usuario': request.data.get('id_usuario')
        }
        serializer = MascotaSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
