# Generated by Django 4.2.6 on 2023-10-31 13:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0005_accommodationfeature_description_en_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accommodationpicture',
            options={'verbose_name': 'Accommodation picture', 'verbose_name_plural': 'Accommodation pictures'},
        ),
        migrations.AddField(
            model_name='accommodation',
            name='long_description_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Long description'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='long_description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Long description'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='long_description_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Long description'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='short_description_en',
            field=models.TextField(null=True, verbose_name='Short description'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='short_description_ru',
            field=models.TextField(null=True, verbose_name='Short description'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='short_description_uz',
            field=models.TextField(null=True, verbose_name='Short description'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='title_en',
            field=models.CharField(max_length=128, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='title_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='title_uz',
            field=models.CharField(max_length=128, null=True, verbose_name='Title'),
        ),
    ]
