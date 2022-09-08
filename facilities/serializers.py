from rest_framework import serializers
from users.serializers import UserSerializer

from .models import Facility


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = "__all__"
        read_only_fields = ["id"]
        depth = 1
    user = UserSerializer(read_only=True)
    # addres = AddresSerializer(read_only=True)
