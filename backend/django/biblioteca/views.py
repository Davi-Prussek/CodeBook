from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

# Create your views here.

class CodigoViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    filterset_fields = ['linguagem']
    def get_queryset(self):
        return Codigo.objects.filter(usuarios=self.request.user)
