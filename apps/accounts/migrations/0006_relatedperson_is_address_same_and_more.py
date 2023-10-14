# Generated by Django 4.2.6 on 2023-10-14 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatedperson',
            name='is_address_same',
            field=models.BooleanField(default=0, verbose_name='Is address the same?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relatedperson',
            name='is_phone_number_same',
            field=models.BooleanField(default=0, verbose_name='Is phone number the same?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relatedperson',
            name='responsible',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='related_people', to=settings.AUTH_USER_MODEL, verbose_name='Responsible person'),
            preserve_default=False,
        ),
    ]