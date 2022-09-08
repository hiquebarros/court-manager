from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Address
from .serializers import AddressSerializer
from facilities.models import Facility

class AddressView(generics.RetrieveUpdateAPIView, generics.CreateAPIView):
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        facility_instance = get_object_or_404(Facility, pk=self.kwargs["facility_id"])
        serializer.save(facility=facility_instance)

    def get_queryset(self):
        facility_instance = get_object_or_404(Facility, pk=self.kwargs["facility_id"])
        return Address.objects.filter(facility=facility_instance)