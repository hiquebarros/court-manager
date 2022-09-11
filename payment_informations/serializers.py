from .models import Payment_information
from users.serializers import UserSerializer
from rest_framework.serializers import ModelSerializer


class PaymentInformationSerializer(ModelSerializer):
    
    class Meta:
        model= Payment_information
        fields='__all__'
