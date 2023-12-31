# Generated by Django 4.2.6 on 2023-12-05 06:43

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonenumber',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Active status'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Phone number'),
        ),
    ]
