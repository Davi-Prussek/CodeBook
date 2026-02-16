from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

# Create your views here.

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['linguagem']

class CodigoViewSet(ModelViewSet):
    queryset = Codigo.objects.all()
    serializer_class = CodigoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categoria', 'categoria__linguagem']