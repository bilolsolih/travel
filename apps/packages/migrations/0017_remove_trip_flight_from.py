# Generated by Django 4.2.6 on 2023-11-20 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0016_alter_trip_flight_from'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='flight_from',
        ),
    ]