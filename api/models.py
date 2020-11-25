'''
    TODO:
        - Crear modelo Usuario ------------------ [x]
        - Crear modelo Mascota ------------------ [x]
        - Crear modelo Mascota_perdida ---------- [x]
        - Crear modelo Mascota_encontrada ------- [x]
        - Crear modelo Reporte ------------------ [x]
        - Crear modelo Reporte_perdido ---------- [x]
        - Crear modelo Reporte_avistado --------- [x]
        - Crear modelo Reporte_encontrado ------- [x]
        - Relacionar modelos -------------------- [x]
'''

from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


'''-------| Create your models here. |-------'''


# Administrar cuentas
# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError(
#                 "Los usuarios deben tener un correo electronico asociado")
#         if not username:
#             raise ValueError("Los usuarios deben tener un nombre de usuario")

#         user = self.model(
#             email=self.normalize_email(email),
#             username=username
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             password=password,
#             username=username
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user


# Modelo para registrar usuario con datos principales
# class UsuarioRegistro(AbstractBaseUser):
#     email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     date_joined = models.DateTimeField(
#         verbose_name='date joined', auto_now_add=True)
#     last_login = models.DateTimeField(
#         verbose_name='last login', auto_now_add=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']

#     objects = MyAccountManager()

#     def __str__(self):
#         return self.username

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, app_label):
#         return True


# Modelo de clase de Usuario.
class Usuario(models.Model):
    id_usuario = models.AutoField(
        unique=True,
        primary_key=True
    )
    correo_duenio = models.EmailField(max_length=100, unique=True)  # Email
    nombre_duenio = models.CharField(max_length=100)  # String
    pais = models.CharField(max_length=100)  # String
    ciudad = models.CharField(max_length=100)  # String
    colonia = models.CharField(max_length=100)  # String
    calle = models.CharField(max_length=100)  # String
    numero = models.CharField(max_length=100)  # String

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

    id_usuario = models.ForeignKey(
        Usuario,
        default=None,
        db_column="id_usuario",
        verbose_name="usuario",
        on_delete=models.CASCADE
    )  # Foreign Key

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

    id_mascota = models.ForeignKey(
        Mascota,
        default=None,
        verbose_name="mascota",
        db_column="id_mascota",
        on_delete=models.SET_DEFAULT
    )  # Foreign Key

    class Meta:
        verbose_name_plural = "mascota_perdida"

    def __str__(self):
        pass


# Modelo para mascota encontrada.
class Mascota_encontrada(models.Model):
    id_mascota_encontrada = models.AutoField(
        unique=True,
        primary_key=True
    )

    id_mascota = models.ForeignKey(
        Mascota,
        default=None,
        db_column="id_mascota",
        verbose_name="mascota",
        on_delete=models.SET_DEFAULT
    )  # Foreign Key

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

    id_usuario = models.ForeignKey(
        Usuario,
        default=None,
        db_column="id_usuario",
        verbose_name="usuario",
        on_delete=models.CASCADE
    )  # Foreign Key
    id_mascota = models.ForeignKey(
        Mascota,
        default=None,
        db_column="id_mascota",
        verbose_name="mascota",
        on_delete=models.CASCADE
    )  # Foreign Key

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

    id_reporte = models.ForeignKey(
        Reporte,
        default=None,
        db_column="id_reporte",
        verbose_name="reporte",
        on_delete=models.SET_DEFAULT
    )  # Foreign Key

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

    id_reporte = models.ForeignKey(
        Reporte,
        default=None,
        db_column="id_reporte",
        verbose_name="reporte",
        on_delete=models.SET_DEFAULT
    )  # Foreign Key

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

    id_reporte = models.ForeignKey(
        Reporte,
        default=None,
        db_column="id_reporte",
        verbose_name="reporte",
        on_delete=models.SET_DEFAULT
    )  # Foreign Key

    class Meta:
        verbose_name_plural = "reporte_perdido"

    def __str__(self):
        return self.ultimo_lugar_visto
