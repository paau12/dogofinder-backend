from rest_framework import serializers
from .models import *


class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'


class Usuario_serializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
