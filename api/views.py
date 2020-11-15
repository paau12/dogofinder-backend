'''
    TODO:
        |----------------------------------------|  A  |  R  |  M  |  C  |
        |- Crear view Usuario ------------------ | [x] | [ ] | [ ] | [ ] |
        |- Crear view Mascota ------------------ | [x] | [x] | [x] | [x] |
        |- Crear view Mascota_perdida ---------- | [x] | [x] | [x] | [x] |
        |- Crear view Mascota_encontrada ------- | [x] | [x] | [x] | [x] |
        |- Crear view Reporte ------------------ | [x] | [x] | [x] | [x] |
        |- Crear view Reporte_avistado --------- | [x] | [x] | [x] | [x] |
        |- Crear view Reporte_perdido ---------- | [x] | [x] | [x] | [x] |
        |- Crear view Reporte_encontrado ------- | [x] | [x] | [x] | [x] |
        |----------------------------------------------------------------|
        |- A: Actualizar.                                                |
        |- R: Remover.                                                   |
        |- M: Modificar.                                                 |
        |- C: Consultar.                                                 |
        |----------------------------------------------------------------|
'''


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


''' --------| Views para clase Reporte. |-------- '''


# Agrega un objeto reporte a la base de datos.
@api_view(['POST'])
def post_reporte(request):
    data = {
        'fecha_reporte': request.data.get('fecha_reporte'),
        'descripcion_reporte': request.data.get('descripcion_reporte'),
        'id_usuario': request.data.get('id_usuario'),
        'id_mascota': request.data.get('id_mascota'),
    }
    serializer = Reporte_serializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Elimina, modifica y retorna un objeto reporte.
@api_view(['GET', 'PUT', 'DELETE'])
def GPD_reporte(request, id):

    try:
        # Se trata de cargar un objeto Usuario.
        reporte = Reporte.objects.get(id_reporte=id)

    except Reporte.DoesNotExist:
        # Si este no existe se retorna una excepcion 404.
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Si el request es de tipo GET, se retorna el objeto con
        # todos todos sus campos.
        reporte_serializado = Reporte_serializer(reporte)
        return Response(reporte_serializado.data)

    elif request.method == 'PUT':
        # Si el request es de tipo PUT, se actualizan los campos del
        # objeto.
        serializer = Reporte_serializer(reporte, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Si el request es de tipo DELETE, se elimina el objeto de
        # la base de datos.
        reporte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


''' --------| Views para clase Reporte_avistado. |-------- '''


# Agrega un objeto reporte a la base de datos.
@api_view(['POST'])
def post_reporte_avistado(request):
    data = {
        'lugar_avistado': request.data.get('lugar_avistado'),
        'imagen_avistamiento': request.data.get('imagen_avistamiento'),
        'id_reporte': request.data.get('id_reporte'),
    }
    serializer = Reporte_avistado_serializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Elimina, modifica y retorna un objeto reporte.
@api_view(['GET', 'PUT', 'DELETE'])
def GPD_reporte_avistado(request, id):

    try:
        # Se trata de cargar un objeto Usuario.
        reporte_avistado = Reporte_avistado.objects.get(id_reporte=id)

    except Reporte_avistado.DoesNotExist:
        # Si este no existe se retorna una excepcion 404.
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Si el request es de tipo GET, se retorna el objeto con
        # todos todos sus campos.
        reporte_avistado_serializado = Reporte_avistado_serializer(
            reporte_avistado)
        return Response(reporte_avistado_serializado.data)

    elif request.method == 'PUT':
        # Si el request es de tipo PUT, se actualizan los campos del
        # objeto.
        serializer = Reporte_avistado_serializer(
            reporte_avistado, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Si el request es de tipo DELETE, se elimina el objeto de
        # la base de datos.
        reporte_avistado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


''' --------| Views para clase Reporte_encontrado. |-------- '''


# Agrega un objeto reporte a la base de datos.
@api_view(['POST'])
def post_reporte_encontrado(request):
    data = {
        'lugar_encontrado': request.data.get('lugar_encontrado'),
        'imagen_encontrado': request.data.get('imagen_encontrado'),
        'mascota_recojida': request.data.get('mascota_recojida'),
        'id_reporte': request.data.get('id_reporte'),
    }
    serializer = Reporte_encontrado_serializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Elimina, modifica y retorna un objeto reporte.
@api_view(['GET', 'PUT', 'DELETE'])
def GPD_reporte_encontrado(request, id):

    try:
        # Se trata de cargar un objeto Usuario.
        reporte_encontrado = Reporte_encontrado.objects.get(id_reporte=id)

    except Reporte_encontrado.DoesNotExist:
        # Si este no existe se retorna una excepcion 404.
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Si el request es de tipo GET, se retorna el objeto con
        # todos todos sus campos.
        reporte_encontrado_serializado = Reporte_encontrado_serializer(
            reporte_encontrado)
        return Response(reporte_encontrado_serializado.data)

    elif request.method == 'PUT':
        # Si el request es de tipo PUT, se actualizan los campos del
        # objeto.
        serializer = Reporte_encontrado_serializer(
            reporte_encontrado, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Si el request es de tipo DELETE, se elimina el objeto de
        # la base de datos.
        reporte_encontrado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


''' --------| Views para clase Reporte_encontrado. |-------- '''


# Agrega un objeto reporte a la base de datos.
@api_view(['POST'])
def post_reporte_perdido(request):
    data = {
        'ultimo_lugar_visto': request.data.get('ultimo_lugar_visto'),
        'id_reporte': request.data.get('id_reporte'),
    }
    serializer = Reporte_perdido_serializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Elimina, modifica y retorna un objeto reporte.
@api_view(['GET', 'PUT', 'DELETE'])
def GPD_reporte_perdido(request, id):

    try:
        # Se trata de cargar un objeto Usuario.
        reporte_perdido = Reporte_perdido.objects.get(id_reporte=id)

    except Reporte_perdido.DoesNotExist:
        # Si este no existe se retorna una excepcion 404.
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Si el request es de tipo GET, se retorna el objeto con
        # todos todos sus campos.
        reporte_perdido_serializado = Reporte_perdido_serializer(
            reporte_perdido)
        return Response(reporte_perdido_serializado.data)

    elif request.method == 'PUT':
        # Si el request es de tipo PUT, se actualizan los campos del
        # objeto.
        serializer = Reporte_perdido_serializer(
            reporte_perdido, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Si el request es de tipo DELETE, se elimina el objeto de
        # la base de datos.
        reporte_perdido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


''' --------| Views para clase Usuario. |-------- '''


# Agrega un objeto usuario a la base de datos.
@api_view(['POST'])
def post_usuario(request):
    data = {
        'correo_duenio': request.data.get('correo_duenio'),
        'nombre_duenio': request.data.get('nombre_duenio'),
        'pais': request.data.get('pais'),
        'ciudad': request.data.get('ciudad'),
        'colonia': request.data.get('colonia'),
        'calle': request.data.get('calle'),
        'numero': request.data.get('numero'),
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
        serializer = Mascota_serializer(mascota)
        return Response(serializer.data)

    # Eliminar una mascota
    elif request.method == 'DELETE':
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Actualizar detalles de una mascota
    elif request.method == 'PUT':
        serializer = Mascota_serializer(mascota, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_mascotas(request):
    # Obtener todas las mascotas
    if request.method == 'GET':
        mascotas = Mascota.objects.all()
        serializer = Mascota_serializer(mascotas, many=True)
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
        serializer = Mascota_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


''' --------| Views para clase Mascota_perdida. |-------- '''


# Agrega un objeto mascota_perdida a la base de datos.
@api_view(['POST'])
def post_mascota_perdida(request):
    data = {
        'id_mascota': request.data.get('id_mascota'),
    }
    serializer = Mascota_perdida_serializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Elimina, modifica y retorna un objeto mascota_perdida.
@api_view(['GET', 'PUT', 'DELETE'])
def GPD_mascota_perdida(request, id):

    try:
        # Se trata de cargar un objeto Usuario.
        mascota_perdida = Mascota_perdida.objects.get(id_mascota_perdida=id)

    except Mascota_perdida.DoesNotExist:
        # Si este no existe se retorna una excepcion 404.
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Si el request es de tipo GET, se retorna el objeto con
        # todos todos sus campos.
        mascota_perdida_serializado = Mascota_perdida_serializer(
            mascota_perdida)
        return Response(mascota_perdida_serializado.data)

    elif request.method == 'PUT':
        # Si el request es de tipo PUT, se actualizan los campos del
        # objeto.
        serializer = Mascota_perdida_serializer(
            mascota_perdida, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Si el request es de tipo DELETE, se elimina el objeto de
        # la base de datos.
        mascota_perdida.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


''' --------| Views para clase Mascota_encontrada. |-------- '''


# Agrega un objeto mascota_encontrada a la base de datos.
@api_view(['POST'])
def post_mascota_encontrada(request):
    data = {
        'id_mascota': request.data.get('id_mascota'),
    }
    serializer = Mascota_encontrada_serializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Elimina, modifica y retorna un objeto mascota_encontrada.
@api_view(['GET', 'PUT', 'DELETE'])
def GPD_mascota_encontrada(request, id):

    try:
        # Se trata de cargar un objeto Usuario.
        mascota_encontrada = Mascota_encontrada.objects.get(
            id_mascota_encontrada=id)

    except Mascota_encontrada.DoesNotExist:
        # Si este no existe se retorna una excepcion 404.
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Si el request es de tipo GET, se retorna el objeto con
        # todos todos sus campos.
        mascota_encontrada_serializado = Mascota_encontrada_serializer(
            mascota_encontrada)
        return Response(mascota_encontrada_serializado.data)

    elif request.method == 'PUT':
        # Si el request es de tipo PUT, se actualizan los campos del
        # objeto.
        serializer = Mascota_encontrada_serializer(
            mascota_encontrada, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Si el request es de tipo DELETE, se elimina el objeto de
        # la base de datos.
        mascota_encontrada.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
