from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Mascota)
admin.site.register(Usuario)
admin.site.register(UsuarioRegistro)  # Nuevo
admin.site.register(Mascota_perdida)
admin.site.register(Mascota_encontrada)
admin.site.register(Reporte)
admin.site.register(Reporte_avistado)
admin.site.register(Reporte_perdido)
admin.site.register(Reporte_encontrado)
