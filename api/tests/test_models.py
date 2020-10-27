from django.test import TestCase
from ..models import Mascota


class MascotaTest(TestCase):
    """ Test Module para modelo de Mascota """

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
            descripcion_mascota="Laika es una chihuahua pequeña.",
            codigo_qr="128391239123",
            in_home=False,
            id_usuario="1234567"
        )

    def test_mascota_raza(self):
        mascota_laika = Mascota.objects.get(nombre_mascota='Laika')
        mascota_missy = Mascota.objects.get(nombre_mascota='Missy')

        self.assertEqual(
            mascota_laika.get_breed(), "Laika es un perro de raza Chiweenie."
        )

        self.assertEqual(
            mascota_missy.get_breed(), "Missy es un perro de raza Chihuahua."
        )
