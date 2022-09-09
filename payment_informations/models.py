from django.db import models
import uuid
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django_cryptography.fields import encrypt


class Payment_information(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    number= encrypt(CardNumberField(('card number')))
    code = encrypt(SecurityCodeField(('security code')))
    expiration_date =encrypt(models.CharField(max_length=250))
    user= models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='payment_informations', null=True)