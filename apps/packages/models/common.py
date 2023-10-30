from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.models import TimeStampedModel


class Day(TimeStampedModel):
    package = models.ForeignKey('packages.Package', related_name='days', on_delete=models.CASCADE, verbose_name=_('Package'))
    ordinal_number = models.PositiveIntegerField(_('Ordinal number'))
    activities = models.ManyToManyField('packages.Activity', related_name='days', verbose_name=_('Activities'))

    class Meta:
        verbose_name = _('Day')
        verbose_name_plural = _('Days')

    def __str__(self):
        return f'{self.package.title}: day {self.ordinal_number}'


class Flight(TimeStampedModel):
    day = models.ForeignKey('packages.Day', related_name='flights', on_delete=models.CASCADE, verbose_name=_('Day'))
    from_city = models.ForeignKey('base.City', related_name='from_flights', on_delete=models.PROTECT, verbose_name=_('From what city?'))
    to_city = models.ForeignKey('base.City', related_name='to_flights', on_delete=models.PROTECT, verbose_name=_('To what city?'))
    flight_time = models.TimeField(_('Flight time'))

    class Meta:
        verbose_name = _('Flight')
        verbose_name_plural = _('FLights')

    def __str__(self):
        return f'From {self.from_city} to {self.to_city} at {self.flight_time} on day {self.day.ordinal_number} of {self.day.package.title}'


class PackageFeature(models.Model):
    title = models.CharField(_('Title'), max_length=128)
    description = RichTextField(_('Description'), blank=True, null=True)
    icon = models.ImageField(_('Icon'), upload_to='images/packages/features/')

    class Meta:
        verbose_name = _('Plan feature')
        verbose_name_plural = _('Plan features')

    def __str__(self):
        return self.title


class Activity(TimeStampedModel):
    title = models.CharField(_('Title'), max_length=256)
    address = models.CharField(_('Address'), max_length=256)
    landmark = models.CharField(_('Landmark'), max_length=256, blank=True, null=True)
    description = RichTextField(_('Description'), blank=True, null=True)

    iframe = models.TextField(_('iFrame'), blank=True, null=True)
    latitude = models.CharField(_('Latitude'), max_length=64, blank=True, null=True)
    longitude = models.CharField(_('Longitude'), max_length=64, blank=True, null=True)

    class Meta:
        verbose_name = _('Activity')
        verbose_name_plural = _('Activities')

    def __str__(self):
        return self.title


__all__ = ['Day', 'Flight', 'PackageFeature', 'Activity']
