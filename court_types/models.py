from django.db import models
import uuid

class Court_type(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    sport = models.CharField(max_length=60)
    type = models.CharField(max_length=60)
    