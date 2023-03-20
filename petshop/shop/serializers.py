from rest_framework import serializers
from rest_framework.response import Response

from .models import *

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderOf
        fields = '__all__'