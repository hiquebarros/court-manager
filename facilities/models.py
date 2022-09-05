from django.db import models
import uuid

class Facility(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="facilities"
    )
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=60)
    address = models.OneToOneField("addresses.Address", on_delete=models.CASCADE)
