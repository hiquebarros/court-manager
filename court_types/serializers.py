from rest_framework import serializers
from .models import Court_type

class Court_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court_type
        fields = '__all__'

        