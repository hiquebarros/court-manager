from rest_framework import serializers

from courts.models import Court, NonOperatingDays, Holiday
from schedules.models import Schedule

from datetime import datetime, timedelta
import pandas as pd
import ipdb

from users.serializers import UserBaseInfoSerializer


def get_week_day(day):
    days_of_the_week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

    return days_of_the_week[day]


class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = "__all__"


class NonOperatingDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonOperatingDays
        fields = "__all__"
        read_only_fields = ["court"]
    

class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = "__all__"
        read_only_fields = ["court"]


class CourtAvailableSchedulesSerializers(serializers.ModelSerializer):
    available_hours = serializers.SerializerMethodField()

    class Meta:
        model = Court
        fields = ["id", "available_hours", "price_by_hour", "capacity", "is_indoor", "opening_hour", "closing_hour", "court_type", "sport_facility"]


    def get_available_hours(self, obj):
        input_str = self.context.get('request').parser_context.get('kwargs').get('date')
        input_date = datetime.strptime(input_str, '%Y-%m-%d')
        today = datetime.now()
        
        if input_date.date() < today.date():
            return {"detail": "You can't schedule in the past... yet"}
        # ipdb.set_trace()
        month_range = vars(obj)['max_schedule_range_in_months']

        # if input_date.date() > today.date() + pd.DateOffset(month=month_range):
        if input_date.date() > today.date() + timedelta(days=30*month_range):
            return {"detail": "You can't schedule that long in the future... yet"} 
    
        court_id = vars(obj)['id']
        
        weekday = input_date.weekday()
        
        non_operating_day = NonOperatingDays.objects.filter(court_id=court_id, regular_day_off=get_week_day(weekday))
        holiday = Holiday.objects.filter(court_id=court_id, holidays=input_date)
        
        is_after_hours = (input_date.date() == today.date()) and (today.hour > obj.closing_hour.hour)
        
        if non_operating_day  or holiday or is_after_hours:
            return {"detail": "court is closed"}
        
        starting_hour = obj.opening_hour.hour
        
        if input_date.date() == today.date():
            starting_hour = today.hour + 1
        
        schedules_booked = Schedule.objects.filter(datetime__date=input_date)
        booked_hours = [schedule.datetime.hour for schedule in schedules_booked]
        
        return [hour for hour in range(starting_hour, obj.closing_hour.hour) if hour not in booked_hours]
        