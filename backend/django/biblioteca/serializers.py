from rest_framework.serializers import ModelSerializer
from .models import *

class CodigoSerializer(ModelSerializer):
    class Meta:
        model = Codigo
        fields = "__all__"
