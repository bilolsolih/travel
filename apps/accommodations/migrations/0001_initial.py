# Generated by Django 4.2.6 on 2023-10-28 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('address', models.CharField(max_length=256, verbose_name='Address')),
                ('landmark', models.CharField(blank=True, max_length=256, null=True, verbose_name='Landmark')),
                ('iframe', models.TextField(blank=True, null=True, verbose_name='iFrame')),
                ('latitude', models.CharField(blank=True, max_length=64, null=True, verbose_name='Latitude')),
                ('longitude', models.CharField(blank=True, max_length=64, null=True, verbose_name='Longitude')),
            ],
            options={
                'verbose_name': 'Accommodation',
                'verbose_name_plural': 'Accommodations',
            },
        ),
        migrations.CreateModel(
            name='AccommodationFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('icon', models.ImageField(upload_to='images/accommodations/features/', verbose_name='Icon')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Is paid?')),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
            },
        ),
        migrations.CreateModel(
            name='AccommodationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('picture', models.ImageField(upload_to='images/accommodations/accommodation_types/', verbose_name='Picture')),
            ],
            options={
                'verbose_name': 'Accommodation type',
                'verbose_name_plural': 'Accommodation types',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='accommodations.country', verbose_name='Country')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='AccommodationPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('picture', models.ImageField(upload_to='images/accommodations/destinations/%Y/%m/%d/', verbose_name='Picture')),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pictures', to='accommodations.accommodation', verbose_name='Accommodation')),
            ],
            options={
                'verbose_name': 'Accommodation type',
                'verbose_name_plural': 'Accommodation types',
            },
        ),
        migrations.AddField(
            model_name='accommodation',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='accommodations', to='accommodations.city', verbose_name='City'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='accommodations', to='accommodations.country', verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='features',
            field=models.ManyToManyField(blank=True, related_name='accommodations', to='accommodations.accommodationfeature'),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='accommodations', to='accommodations.accommodationtype', verbose_name='Type'),
        ),
    ]
