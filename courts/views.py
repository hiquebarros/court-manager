from rest_framework import generics
from courts.models import Court, Holiday, NonOperatingDays
from courts.serializers import CourtSerializer, CourtAvailableSchedulesSerializers, NonOperatingDaysSerializer, HolidaySerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import Response
from django.shortcuts import get_object_or_404


import ipdb

class CourtView(generics.ListCreateAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer


class CourtAvailableSchedulesView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]

    queryset = Court.objects.all()
    serializer_class = CourtAvailableSchedulesSerializers
    
    lookup_url_kwarg = "court_id"

class RegisterNonOperantingDay(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]

    queryset = NonOperatingDays.objects.all()
    serializer_class = NonOperatingDaysSerializer
    
    lookup_url_kwarg = "court_id"


    def perform_create(self, serializer):
        court_id = self.kwargs[self.lookup_url_kwarg]
        court = get_object_or_404(Court,id=court_id)

        serializer.save(court=court)

class DeleteNonOperantingDay(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]

    queryset = NonOperatingDays.objects.all()
    serializer_class = NonOperatingDaysSerializer
    
    lookup_url_kwarg = "non_operanting_day_id"


class RegisterHolidayView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]

    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    
    lookup_url_kwarg = "court_id"


    def perform_create(self, serializer):
        court_id = self.kwargs[self.lookup_url_kwarg]
        court = get_object_or_404(Court,id=court_id)

        serializer.save(court=court)

class DeleteHolidayView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]

    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    
    lookup_url_kwarg = "holiday_id"