# Generated by Django 4.2.6 on 2023-11-20 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0013_remove_trip_flight_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='flight_from',
            field=models.CharField(default='Tashkent', max_length=123),
            preserve_default=False,
        ),
    ]