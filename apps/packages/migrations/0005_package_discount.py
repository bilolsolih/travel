# Generated by Django 4.2.6 on 2023-10-13 08:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0004_activity_description_alter_planfeature_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='discount',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Discount'),
        ),
    ]