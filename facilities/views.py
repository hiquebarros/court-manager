from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from facilities.models import Facility

from .permissions import IsAOwner, IsAOwnOwner, IsAOwnOwnerOrAdmin
from .serializers import FacilitySerializer


class FacilityView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAOwner]
    serializer_class = FacilitySerializer
    queryset = Facility.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FacilityDetailView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAOwnOwner]
    serializer_class = FacilitySerializer
    queryset = Facility.objects.all()
    lookup_url_kwarg = "sport_facility_id"

class FacilityDeleteView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAOwnOwnerOrAdmin]
    serializer_class = FacilitySerializer
    queryset = Facility.objects.all()
    lookup_url_kwarg = "sport_facility_id"
