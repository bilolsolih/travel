# Generated by Django 4.2.6 on 2023-10-12 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0002_remove_package_end_date_remove_package_start_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active status'),
        ),
    ]
