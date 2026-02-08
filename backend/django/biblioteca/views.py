from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

# Create your views here.

class CodigoViewSet(ModelViewSet):
    queryset = Codigo.objects.all()
    serializer_class = CodigoSerializer
