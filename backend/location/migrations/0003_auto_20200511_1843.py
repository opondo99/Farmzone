# Generated by Django 3.0.6 on 2020-05-11 18:43

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_location_coordinates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='coordinates',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), blank=True, default=list, size=2),
        ),
    ]
