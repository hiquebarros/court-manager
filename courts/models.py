from django.db import models
import uuid

class Court(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    capacity = models.IntegerField()
    is_indoor = models.BooleanField(default=False)
  
    court_type = models.ForeignKey("court_types.Court_type", on_delete=models.CASCADE, related_name="courts", null=True)
    sport_facility = models.ForeignKey("facilities.Facility", on_delete=models.CASCADE, related_name="courts")