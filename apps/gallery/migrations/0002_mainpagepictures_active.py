# Generated by Django 4.2.6 on 2023-10-14 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpagepictures',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active status'),
        ),
    ]