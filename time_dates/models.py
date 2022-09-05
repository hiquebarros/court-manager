from django.db import models
import uuid

class Time_date(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    court = models.ForeignKey(
        "courts.Court", on_delete=models.CASCADE, related_name="time_dates"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateField()
    is_available = models.BooleanField()