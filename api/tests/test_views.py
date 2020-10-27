import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Mascota
from ..serializers import MascotaSerializer


# Initialize APIClient app
client = Client()
