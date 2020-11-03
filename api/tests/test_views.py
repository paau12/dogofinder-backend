import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Mascota
from ..serializers import MascotaSerializer


# Initialize APIClient app
client = Client()


# Test - Verify fetched records
class GetAllMascotasTest(TestCase):
    """
        Test Module to GET all mascotas API
    """

    def setUp(self):
        Mascota.objects.create(
            nombre_mascota="Laika",
            tipo_mascota="Perro",
            raza_mascota="Chiweenie",
            descripcion_mascota="Laika es un chiweenie pequeño.",
            codigo_qr="1233456643",
            in_home=True,
            id_usuario="1234567"
        )

        Mascota.objects.create(
            nombre_mascota="Missy",
            tipo_mascota="Perro",
            raza_mascota="Chihuahua",
            descripcion_mascota="Missy es una chihuahua pequeña.",
            codigo_qr="2313213123",
            in_home=False,
            id_usuario="1234567"
        )

        Mascota.objects.create(
            nombre_mascota="Emi",
            tipo_mascota="Perro",
            raza_mascota="Minitoy",
            descripcion_mascota="Emi es una mini-toy pequeña.",
            codigo_qr="128392321",
            in_home=True,
            id_usuario="1234567"
        )

    def test_get_all_mascotas(self):
        # get API response
        response = client.get(reverse('get_post_mascotas'))

        # get data from db
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Test - Insert mascotas
class CreateNewMascotaTest(TestCase):
    """
        Test Module for inserting a new mascota
    """

    def setUp(self):
        self.valid_payload = {
            'nombre_mascota': "Missy",
            'tipo_mascota': "Perro",
            'raza_mascota': "Chihuahua",
            'descripcion_mascota': "Laika es una chihuahua pequeña.",
            'codigo_qr': "128391239123",
            'in_home': False,
            'id_usuario': "1234567"
        }

        self.invalid_payload = {
            'nombre_mascota': "",
            'tipo_mascota': "Perro",
            'raza_mascota': "Chihuahua",
            'descripcion_mascota': "Laika es una chihuahua pequeña.",
            'codigo_qr': "128391239123",
            'in_home': False,
            'id_usuario': "1234567"
        }

    def test_create_valid_mascota(self):
        response = client.post(
            reverse('get_post_mascotas'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_mascota(self):
        response = client.post(
            reverse('get_post_mascotas'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# Test - Update single Mascota
class UpdateSingleMascotaTest(TestCase):
    """
        Test module for updating an existing Mascota record.
    """

    def setUp(self):
        self.laika = Mascota.objects.create(
            nombre_mascota="Laika",
            tipo_mascota="Perro",
            raza_mascota="Chiweenie",
            descripcion_mascota="Laika es una perra de raza pequeña.",
            codigo_qr="1231231212",
            in_home=True,
            id_usuario="312324123"
        )

        self.missy = Mascota.objects.create(
            nombre_mascota="Missy",
            tipo_mascota="Perro",
            raza_mascota="Chihuahua",
            descripcion_mascota="Missy es una chihuahua pequeña.",
            codigo_qr="1231231212",
            in_home=True,
            id_usuario="312324123"
        )

        self.valid_payload = {
            'nombre_mascota': "Laika",
            'tipo_mascota': "Perro",
            'raza_mascota': "Chihuahua",
            'descripcion_mascota': "Laika es una chihuahua pequeña.",
            'codigo_qr': "128391239123",
            'in_home': False,
            'id_usuario': "1234567"
        }

        self.invalid_payload = {
            'nombre_mascota': "",
            'tipo_mascota': "Gato",
            'raza_mascota': "Labrador",
            'descripcion_mascota': "Es una chihuahua pequeña.",
            'codigo_qr': "12382831",
            'in_home': True,
            'id_usuario': "12312312"
        }

    def test_valid_update_mascota(self):
        response = client.put(
            reverse('get_delete_update_mascota', kwargs={'pk': self.laika.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_mascota(self):
        response = client.put(
            reverse('get_delete_update_mascota', kwargs={'pk': self.laika.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# Test - Delete single Mascota
class DeleteSingleMascotaTest(TestCase):
    """
        Test module for deleting an existing mascota record.
    """

    def setUp(self):
        self.laika = Mascota.objects.create(
            nombre_mascota="Laika",
            tipo_mascota="Perro",
            raza_mascota="Chiweenie",
            descripcion_mascota="Laika es una perra de raza pequeña.",
            codigo_qr="1231231212",
            in_home=True,
            id_usuario="312324123"
        )

        self.missy = Mascota.objects.create(
            nombre_mascota="Missy",
            tipo_mascota="Perro",
            raza_mascota="Chihuahua",
            descripcion_mascota="Missy es una chihuahua pequeña.",
            codigo_qr="1231231212",
            in_home=True,
            id_usuario="312324123"
        )

    def test_valid_delete_mascota(self):
        response = client.delete(
            reverse('get_delete_update_mascota', kwargs={'pk': self.laika.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_mascota(self):
        response = client.delete(
            reverse('get_delete_update_mascota', kwargs={'pk': 30})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
