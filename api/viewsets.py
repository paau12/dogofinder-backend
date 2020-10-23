from rest_framework import viewsets
from . import models
from . import serializers


class MascotaViewset(viewsets.ModelViewSet):
    queryset = models.Mascota.objects.all()
    serializer_class = serializers.MascotaSerializer
