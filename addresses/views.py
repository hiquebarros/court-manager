from django.shortcuts import get_object_or_404
from rest_framework import generics
from addresses.permissions import IsFacilityOwner, IsOwnerOrReadOnly
from .models import Address
from .serializers import AddressSerializer
from facilities.models import Facility
from rest_framework.views import Response, Request, status
from rest_framework.exceptions import ValidationError
from rest_framework.authentication import TokenAuthentication

class AddressView(generics.RetrieveUpdateAPIView, generics.CreateAPIView):
    serializer_class = AddressSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsFacilityOwner, IsOwnerOrReadOnly]
    queryset = Facility.objects.all()

    lookup_url_kwarg = 'facility_id'

    def perform_create(self, serializer):
        repeated_address = Address.objects.filter(street=serializer.validated_data['street'], number=serializer.validated_data['number'], zipcode=serializer.validated_data['zipcode'], state=serializer.validated_data['state'])

        if repeated_address:
            raise ValidationError({"detail": "address already exists."})

        facility_instance = get_object_or_404(Facility, pk=self.kwargs["facility_id"])
        serializer.save()

        facility_instance.address_id = serializer.data['id']
        facility_instance.save()

    def get_object(self):
        facility_instance = get_object_or_404(Facility, pk=self.kwargs["facility_id"])
        self.check_object_permissions(self.request, facility_instance)
        return facility_instance.address


