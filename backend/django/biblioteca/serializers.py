from rest_framework.serializers import ModelSerializer
from .models import *

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class CodigoSerializer(ModelSerializer):
    class Meta:
        model = Codigo
        fields = "__all__"
