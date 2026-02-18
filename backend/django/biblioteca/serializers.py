from rest_framework import serializers
from .models import Codigo, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'linguagem', 'descricao']


class CodigoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)

    class Meta:
        model = Codigo
        fields = [
            'id',
            'nome',
            'descricao',
            'modoDeUsar',
            'categoria',
        ]
