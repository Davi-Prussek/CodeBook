from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

# Create your views here.

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CodigoViewSet(ModelViewSet):
    queryset = Codigo.objects.all()
    serializer_class = CodigoSerializer