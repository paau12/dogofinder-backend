from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def prueba_request(request):
    if request.method == 'GET':
        return Response('Request GET')

    elif request.method == 'PUT':
        return Response('Request PUT')

    elif request.method == 'DELETE':
        return Response('Request DELETE')

    elif request.method == 'POST':
        return Response('Request POST {}'.format(request.data.get('id')))

    else:
        return Response('Request desconocido')


''' --------| Views para clase Usuario. |-------- '''

# Agrega un objeto usuario a la base de datos.
@api_view(['POST'])
def post_usuario(request):
    data = {
        'correo_duenio':request.data.get('correo_duenio'),
        'nombre_duenio':request.data.get('nombre_duenio'),
        'pais':request.data.get('pais'),
        'ciudad':request.data.get('ciudad'),
        'colonia':request.data.get('colonia'),
        'calle':request.data.get('calle'),
        'numero':request.data.get('numero'),
    }
    serializer = Usuario_serializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Elimina, modifica y retorna un objeto usuario.
@api_view(['GET', 'PUT', 'DELETE'])
def GPD_usuario(request, id):

    try:
        # Se trata de cargar un objeto Usuario.
        usuario = Usuario.objects.get(id_usuario=id)

    except Usuario.DoesNotExist:
        # Si este no existe se retorna una excepcion 404.
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Si el request es de tipo GET, se retorna el objeto con
        # todos todos sus campos.
        usuario_serializado = Usuario_serializer(usuario)
        return Response(usuario_serializado.data)

    elif request.method == 'PUT':
        # Si el request es de tipo PUT, se actualizan los campos del
        # objeto.
        serializer = Usuario_serializer(usuario, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Si el request es de tipo DELETE, se elimina el objeto de
        # la base de datos.
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


''' --------| Views para clase Mascota. |-------- '''

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_mascota(request, id):
    try:
        mascota = Mascota.objects.get(id_mascota=id)

    except Mascota.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Obtener detalles de una mascota
    if request.method == 'GET':
        serializer = MascotaSerializer(mascota)
        return Response(serializer.data)

    # Eliminar una mascota
    elif request.method == 'DELETE':
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Actualizar detalles de una mascota
    elif request.method == 'PUT':
        serializer = MascotaSerializer(mascota, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_mascotas(request):
    # Obtener todas las mascotas
    if request.method == 'GET':
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)

    # Insertar un nuevo registro de mascota
    elif request.method == 'POST':
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
