from django.shortcuts import render
from rest_framework import generics
from schedules.models import Schedule
from schedules.serializers import ScheduleSerializer
from courts.models import Court
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
import datetime

import ipdb

class ScheduleCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    
    lookup_url_kwarg = "court_id"


    def perform_create(self, serializer):
        court_id = self.kwargs[self.lookup_url_kwarg]

        court = get_object_or_404(Court, id=court_id)

        serializer.save(user=self.request.user, court=court)

class CancelScheduleView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    
    lookup_url_kwarg = "schedule_id"