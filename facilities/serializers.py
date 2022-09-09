from rest_framework import serializers
from users.serializers import UserSerializer

from .models import Facility


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = "__all__"
        depth = 1
    user = UserSerializer(read_only=True)
