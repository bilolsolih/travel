# Generated by Django 4.2.6 on 2023-11-20 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0015_alter_trip_flight_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='flight_from',
            field=models.CharField(default='Tashkent', max_length=123, null=True),
        ),
    ]