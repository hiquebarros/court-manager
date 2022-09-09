from django.db import models
import uuid

class DayOfTheWeek(models.TextChoices):
    MONDAY = "MONDAY",
    TUESDAY = "TUESDAY",
    WEDNESDAY = "WEDNESDAY",
    THURSDAY = "THURSDAY",
    FRIDAY = "FRIDAY",
    SATURDAY = "SATURDAY",
    SUNDAY = "SUNDAY",
    DEFAULT = "DEFAULT"


class NonOperatingDays(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    court = models.ForeignKey("courts.Court", on_delete=models.CASCADE, related_name="non_operating_days")
    regular_day_off = models.CharField(max_length=9, choices=DayOfTheWeek.choices, default=DayOfTheWeek.DEFAULT)


class Holiday(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    court = models.ForeignKey("courts.Court", on_delete=models.CASCADE, related_name="holidays")
    holidays = models.DateField(null=True, blank=True)

    
class Court(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    capacity = models.IntegerField()
    is_indoor = models.BooleanField(default=False)
    price_by_hour = models.DecimalField(max_digits=10, decimal_places=2)
    max_schedule_range_in_months = models.IntegerField()

    opening_hour = models.TimeField(null=True, blank=True)
    closing_hour = models.TimeField(null=True, blank=True)
    
    court_type = models.ForeignKey("court_types.Court_type", on_delete=models.CASCADE, related_name="courts", null=True, blank=True)
    sport_facility = models.ForeignKey("facilities.Facility", on_delete=models.CASCADE, related_name="courts", null=True, blank=True)