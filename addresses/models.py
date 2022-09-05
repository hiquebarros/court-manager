from django.db import models
import uuid

class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    street = models.CharField(max_length=60)
    number = models.CharField(max_length=10)
    zipcode = models.CharField(max_length=20)
    state = models.CharField(max_length=20)