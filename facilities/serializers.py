from rest_framework import serializers
from users.serializers import UserBaseInfoSerializer

from .models import Facility


class FacilitySerializer(serializers.ModelSerializer):
    user = UserBaseInfoSerializer(read_only=True)
    class Meta:
        model = Facility
        fields = "__all__"
        depth = 1
