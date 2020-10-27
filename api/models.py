from django.db import models

# Create your models here.


# Model - Mascota
class Mascota(models.Model):
    nombre_mascota = models.CharField(max_length=100)  # string
    tipo_mascota = models.CharField(max_length=100)  # string
    raza_mascota = models.CharField(max_length=100)  # string
    descripcion_mascota = models.CharField(max_length=300)  # string
    codigo_qr = models.CharField(max_length=100)  # string
    foto_mascota = models.ImageField(upload_to='api/resources/mascotas',
                                     height_field=None,
                                     width_field=None,
                                     max_length=100)  # image
    in_home = models.BooleanField(default=False)  # boolean
    id_usuario = models.CharField(max_length=100)  # foreign key

    def __str__(self):
        return self.nombre_mascota

    def get_breed(self):
        return self.nombre_mascota + ' es un perro de raza ' + self.raza_mascota + '.'
