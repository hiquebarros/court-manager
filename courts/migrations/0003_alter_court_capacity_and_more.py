# Generated by Django 4.1.1 on 2022-09-13 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courts", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="court",
            name="capacity",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="court",
            name="max_schedule_range_in_days",
            field=models.PositiveIntegerField(),
        ),
    ]
