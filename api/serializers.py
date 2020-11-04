from rest_framework import serializers
from .models import *


''' --------| Serializador para Mascota. |-------- '''

# Serializador para clase Mascota.
class Mascota_serializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'


# Serializador para clase Mascota_perdida.
class Mascota_perdida_serializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota_perdida
        fields = '__all__'


# Serializador para clase Mascota_encontrada.
class Mascota_encontrada_serializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota_encontrada
        fields = '__all__'


''' --------| Serializador para Usuario. |-------- '''

# Serializador para clase Usuario.
class Usuario_serializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


''' --------| Serializador para Reporte. |-------- '''

# Serializador para clase Reporte.
class Reporte_serializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'


# Serializador para clase Reporte_avistado.
class Reporte_avistado_serializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'


# Serializador para clase Reporte_encontrado.
class Reporte_encontrado_serializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'


# Serializador para clase Reporte_perdido.
class Reporte_perdido_serializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'
