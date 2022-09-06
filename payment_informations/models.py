from django.db import models
import uuid

class Payment_information(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    number = models.IntegerField()
    code = models.IntegerField()
    expiration_date = models.DateField()
    

