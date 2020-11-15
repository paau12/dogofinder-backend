from django.contrib import admin

from .models import *

# Register your models here.
admin.register(Mascota)
admin.register(Usuario)  # Nuevo.
admin.register(Mascota_perdida)  # Nuevo.
admin.register(Mascota_encontrada)  # Nuevo.
admin.register(Reporte)  # Nuevo.
admin.register(Reporte_avistado)  # Nuevo.
admin.register(Reporte_perdido)  # Nuevo.
admin.register(Reporte_encontrado)  # Nuevo.
