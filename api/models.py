'''
    TODO:
        - Crear modelo Usuario ------------------ [x]
        - Crear modelo Mascota_perdida ---------- [x]
        - Crear modelo Mascota_encontrada ------- [x]
        - Crear modelo Reporte ------------------ [x]
        - Crear modelo Reporte_perdido ---------- [x]
        - Crear modelo Reporte_avistado --------- [x]
        - Crear modelo Reporte_encontrado ------- [x]
        - Relacionar modelos -------------------- [ ]
'''

from django.db import models

'''-------| Create your models here. |-------'''
# Modelo de clase de Usuario.
class Usuario(models.Model):
    id_usuario = models.AutoField(
        unique=True,
        primary_key=True
    )

    correo_duenio = models.EmailField(max_length=100, unique=True)  # String
    nombre_duenio = models.CharField(max_length=100)  # String
    pais = models.CharField(max_length=100)  # String
    ciudad = models.CharField(max_length=100)  # String
    colonia = models.CharField(max_length=100)  # String
    calle = models.CharField(max_length=100)  # String
    numero = models.CharField(max_length=100)  # String

    #id_mascota = models.ForeignKey(Mascota, default=None, verbose_name='mascota', on_delete=models.SET_DEFAULT)  # Foreign Key

    class Meta:
        verbose_name_plural = "usuario"

    def __str__(self):
        return self.nombre_duenio


'''-------| Modelos de mascotas |-------'''
# Modelo de la clase Mascota.
class Mascota(models.Model):
    id_mascota = models.AutoField(
        unique=True,
        primary_key=True

    )

    nombre_mascota = models.CharField(max_length=100)  # string
    tipo_mascota = models.CharField(max_length=100)  # string
    raza_mascota = models.CharField(max_length=100)  # string
    descripcion_mascota = models.CharField(max_length=300)  # string
    codigo_qr = models.CharField(max_length=100)  # string

    foto_mascota = models.ImageField(
            upload_to='api/resources/mascotas',
            height_field=None,
            width_field=None,
            max_length=100,
            blank=True
        )  # image

    in_home = models.BooleanField(default=False)  # boolean

    id_usuario = models.ForeignKey(Usuario, default=None, verbose_name="usuario", on_delete=models.CASCADE)  # Foreign Key

    class Meta:
        verbose_name_plural = "mascota"

    def __str__(self):
        return self.__nombre_mascota

    def get_breed(self):
        return "{} es un perro de raza {}.".format(self.__mascola, self.__raza)


# Modelo para mascota perdida.
class Mascota_perdida(models.Model):
    id_mascota_perdida = models.AutoField(
        unique=True,
        primary_key=True
    )

    id_mascota = models.ForeignKey(Mascota, default=None, verbose_name="mascota", on_delete=models.SET_DEFAULT)  # Foreign Key
#    id_reporte_perdido = models.ForeignKey(Reporte_perdido, default=None, verbose_name="reporte_perido", on_delete=models.SET_DEFAULT)  # Foreign Key
#    id_reporte_avistado = models.ForeignKey(Reporte_avistado, default=None, verbose_name="reporte_avistado", on_delete=models.SET_DEFAULT)  # Foreign Key

    class Meta:
        verbose_name_plural = "mascota_perdida"

    def __str__(self):
        pass

# Modelo para mascota perdida.
class Mascota_encontrada(models.Model):
    id_mascota_encontrada = models.AutoField(
        unique=True,
        primary_key=True
    )

    id_mascota = models.ForeignKey(Mascota, default=None, verbose_name="mascota", on_delete=models.SET_DEFAULT)  # Foreign Key
#    id_reporte_encontrado = models.ForeignKey(Reporte_avistado, default=None, verbose_name="reporte_encontrado", on_delete=models.SET_DEFAULT)  # Foreign Key

    class Meta:
        verbose_name_plural = "mascota_encontrada"

    def __str__(self):
        pass


'''-------| Modelos de reportes |-------'''
# Modelo de la clase Reporte.
class Reporte(models.Model):
    id_reporte = models.AutoField(
        unique=True,
        primary_key=True
    )

    fecha_reporte = models.DateField()  # Date
    descripcion_reporte = models.CharField(max_length=100)  # String

    id_usuario = models.ForeignKey(Usuario, default=None, verbose_name="usuario", on_delete=models.CASCADE)  # Foreign Key
    id_mascota = models.ForeignKey(Mascota, default=None, verbose_name="mascota", on_delete=models.CASCADE)  # Foreign Key

    class Meta:
        verbose_name_plural = "reporte"

    def __str__(self):
        return self.descripcion_reporte


# Modelo para el reporte de avistamiento de mascota perdida.
class Reporte_avistado(models.Model):
    id_reporte_avistado = models.AutoField(
        unique=True,
        primary_key=True
    )

    lugar_avistado = models.CharField(max_length=100)  # String

    imagen_avistamiento = models.ImageField(
            upload_to='api/resources/mascotas',
            height_field=None,
            width_field=None,
            max_length=100,
            blank=True
        )  # image

    id_reporte = models.ForeignKey(Reporte, default=None, verbose_name="reporte", on_delete=models.SET_DEFAULT)  # Foreign Key

    class Meta:
        verbose_name_plural = "reporte_avistado"

    def __str__(self):
        return self.lugar_avistado


# Modelo para el reporte de mascota encontrada.
class Reporte_encontrado(models.Model):
    id_reporte_encontrado = models.AutoField(
        unique=True,
        primary_key=True
    )

    lugar_encontrado = models.CharField(max_length=100)  # String

    imagen_encontrado = models.ImageField(
            upload_to='api/resources/mascotas',
            height_field=None,
            width_field=None,
            max_length=100,
            blank=True
        )  # image

    mascota_recojida = models.BooleanField(default=False)  # boolean

    id_reporte = models.ForeignKey(Reporte, default=None, verbose_name="reporte", on_delete=models.SET_DEFAULT)  # Foreign Key

    class Meta:
        verbose_name_plural = "reporte_encontrado"

    def __str__(self):
        return self.lugar_encontrado


# Modelo para el reporte de mascota perdida.
class Reporte_perdido(models.Model):
    id_reporte_perdido = models.AutoField(
        unique=True,
        primary_key=True
    )

    ultimo_lugar_visto = models.CharField(max_length=100)  # String

    id_reporte = models.ForeignKey(Reporte, default=None, verbose_name="reporte", on_delete=models.SET_DEFAULT)  # Foreign Key

    class Meta:
        verbose_name_plural = "reporte_perdido"

    def __str__(self):
        return self.ultimo_lugar_visto
