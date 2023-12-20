# Generated by Django 4.2.6 on 2023-12-20 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_title_cr_city_title_uk_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='title_en',
            field=models.CharField(max_length=64, null=True, unique=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='region',
            name='title_ru',
            field=models.CharField(max_length=64, null=True, unique=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='region',
            name='title_uk',
            field=models.CharField(max_length=64, null=True, unique=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='region',
            name='title_uz',
            field=models.CharField(max_length=64, null=True, unique=True, verbose_name='Title'),
        ),
    ]
