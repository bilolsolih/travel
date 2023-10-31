import os
from datetime import timedelta

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.base.models import TimeStampedModel


class Trip(TimeStampedModel):
    package = models.ForeignKey('packages.Package', related_name='trips', on_delete=models.CASCADE, verbose_name=_('Package'))
    start_date = models.DateField(_('Start date'))

    class Meta:
        verbose_name = _('Trip')
        verbose_name_plural = _('Trips')

    @property
    def get_is_active(self):
        return self.start_date > timezone.now()

    @property
    def get_end_date(self):
        return self.start_date + timedelta(days=self.package.get_duration) if self.package.destinations.exists() else None

    def __str__(self):
        return f'{self.package}: {self.start_date} - {self.get_end_date}'


class Package(TimeStampedModel):
    title = models.CharField(_('Title'), max_length=256)
    description = models.TextField(_('Description'), blank=True, null=True)
    picture = models.ImageField(_('Picture'), upload_to='images/packages/packages/%Y/%m/')
    popular_places = models.ManyToManyField('places.PopularPlace', related_name='packages', blank=True, verbose_name=_('Popular places'))

    core_features = models.ManyToManyField('packages.PackageFeature', related_name='packages', blank=True, verbose_name=_('Core features'))

    is_active = models.BooleanField(_('Active status'), default=True)

    class Meta:
        verbose_name = _('Package')
        verbose_name_plural = _('Packages')

    @property
    def get_duration(self):
        if self.destinations.exists():
            return self.destinations.aggregate(total_duration=models.Sum('duration'))['total_duration']
        else:
            return None

    @property
    def get_discount(self):
        return self.plans.aggregate(max_discount=models.Max('discount'))['max_discount'] if self.plans.exists() else None

    def delete(self, *args, **kwargs):
        if os.path.exists(self.picture.path):
            os.remove(self.picture.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title


class Destination(models.Model):
    package = models.ForeignKey('packages.Package', related_name='destinations', on_delete=models.CASCADE, verbose_name=_('Package'))
    country = models.ForeignKey('base.Country', related_name='packages', on_delete=models.PROTECT, verbose_name=_('Country'))
    city = models.ForeignKey('base.City', related_name='packages', on_delete=models.PROTECT, verbose_name=_('City'))
    duration = models.PositiveIntegerField(_('Duration in days'), validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = _('Destination')
        verbose_name_plural = _('Destinations')

    def clean(self):
        if self.city not in self.country.cities.all():
            raise ValidationError({'city': 'No such City in the chosen Country'})

    def __str__(self):
        return f"{self.city} - {self.duration} {'days' if self.duration >= 2 else 'day'}"


__all__ = ['Trip', 'Package', 'Destination']