# Generated by Django 4.2.6 on 2023-10-28 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_user_profile_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifiedPhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='otpcode',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='otpcode',
            name='phone_number',
            field=models.CharField(default='+998912958899', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='otpcode',
            unique_together={('phone_number', 'code', 'is_expired')},
        ),
        migrations.RemoveField(
            model_name='otpcode',
            name='user',
        ),
    ]
