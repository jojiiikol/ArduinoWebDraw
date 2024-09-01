from rest_framework import serializers
from .models import *


class ArduinoMatrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matrix
        fields = ('image', )