from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    is_owner = models.BooleanField(null=True, blank=True, default=False)


    REQUIRED_FIELDS =["first_name", "last_name"]
