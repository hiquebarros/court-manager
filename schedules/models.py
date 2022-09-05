from django.db import models
import uuid

class Schedule(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    time_date = models.ForeignKey(
        "time_dates.Time_date", on_delete=models.CASCADE, related_name="schedules"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="schedules"
    )
    