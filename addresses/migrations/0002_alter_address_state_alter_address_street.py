# Generated by Django 4.1.1 on 2022-09-13 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("addresses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="state",
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name="address",
            name="street",
            field=models.CharField(max_length=127),
        ),
    ]
