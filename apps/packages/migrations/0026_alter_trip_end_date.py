# Generated by Django 4.2.6 on 2023-11-30 13:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0025_trip_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='End date'),
        ),
    ]
