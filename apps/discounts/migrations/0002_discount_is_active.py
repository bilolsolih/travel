# Generated by Django 4.2.6 on 2023-12-05 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active status'),
        ),
    ]