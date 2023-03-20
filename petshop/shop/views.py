from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from django.forms.models import model_to_dict
from .serializers import *
from rest_framework.generics import *

class PetApiView(ListCreateAPIView):
    queryset = Pets.objects.all()
    serializer_class = PetSerializer


class SinglePetView(RetrieveUpdateDestroyAPIView):
    queryset = Pets.objects.all()
    serializer_class = PetSerializer

class OrderView(RetrieveUpdateDestroyAPIView):
    queryset = OrderOf.objects.all()
    serializer_class = OrderSerializer

class OrderApiView(ListCreateAPIView):
    queryset = OrderOf.objects.all()
    serializer_class = OrderSerializer