from rest_framework import serializers
from datetime import datetime, timedelta

from schedules.models import Schedule
from courts.serializers import CourtAvailableSchedulesSerializers
from courts.models import Court, Holiday, NonOperatingDay
from rest_framework.validators import UniqueTogetherValidator

import ipdb


def get_week_day(day):
    days_of_the_week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

    return days_of_the_week[day]


                 

class ScheduleSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = Schedule
        fields = ["id", "datetime", "number_of_hours",  "user", "court"]
        read_only_fields = ["user", "court"]
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Schedule.objects.all(),
        #         fields=["datetime", "court"] 
        #     )
        # ]
    