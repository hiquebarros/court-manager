import uuid

from django.db import models


class Facility(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone_number = models.CharField(max_length=60)

    address = models.OneToOneField("addresses.Address", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="facilities")
