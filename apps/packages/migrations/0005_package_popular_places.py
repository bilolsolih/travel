# Generated by Django 4.2.6 on 2023-10-30 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_popularplace_description_popularplace_picture_and_more'),
        ('packages', '0004_alter_plan_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='popular_places',
            field=models.ManyToManyField(blank=True, related_name='packages', to='places.popularplace', verbose_name='Popular places'),
        ),
    ]
