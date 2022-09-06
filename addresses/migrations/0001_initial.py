# Generated by Django 4.1.1 on 2022-09-05 21:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("street", models.CharField(max_length=60)),
                ("number", models.CharField(max_length=10)),
                ("zipcode", models.CharField(max_length=20)),
                ("state", models.CharField(max_length=20)),
            ],
        ),
    ]
