from ckeditor.fields import RichTextField
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from apps.base.models import TimeStampedModel


class Day(TimeStampedModel):
    package = models.ForeignKey('packages.Package', related_name='days', on_delete=models.CASCADE, verbose_name=_('Package'))
    trip = models.ForeignKey('packages.Trip', related_name='days', on_delete=models.SET_NULL, null=True, verbose_name=_('Trip'))
    day_number = models.PositiveIntegerField(_('Day number'))

    class Meta:
        verbose_name = _('Day')
        verbose_name_plural = _('Days')
        unique_together = ['package', 'trip', 'day_number']
        ordering = ('day_number',)

    @property
    def change_link(self):
        current_site = Site.objects.get_current()

        return mark_safe(f'<a href="http://{current_site.domain}/admin/packages/day/{self.id}/change/">{self.id}</a>')

    def clean(self):
        if not self.package.trips.contains(self.trip):
            raise ValidationError({'trip': 'No such trip in the package.'})

    def __str__(self):
        return f'{self.package.title} - {self.trip.start_date}: day {self.day_number}'


class Stay(TimeStampedModel):
    day = models.ForeignKey('packages.Day', related_name='stays', on_delete=models.CASCADE, verbose_name=_('Day'))
    accommodation = models.ForeignKey('packages.Accommodation', related_name='stays', on_delete=models.PROTECT, verbose_name=_('Accommodation'))
    due_time = models.TimeField(_('Due time'))

    class Meta:
        verbose_name = _('Stay')
        verbose_name_plural = _('Stays')


class Flight(TimeStampedModel):
    day = models.ForeignKey('packages.Day', related_name='flights', on_delete=models.CASCADE, verbose_name=_('Day'))
    from_city = models.ForeignKey('base.City', related_name='from_flights', on_delete=models.PROTECT, verbose_name=_('From what city?'))
    to_city = models.ForeignKey('base.City', related_name='to_flights', on_delete=models.PROTECT, verbose_name=_('To what city?'))
    due_time = models.TimeField(_('Due time'))

    class Meta:
        verbose_name = _('Flight')
        verbose_name_plural = _('Flights')

    def __str__(self):
        return f'From {self.from_city} to {self.to_city} at {self.due_time} on day {self.day.day_number} of {self.day.package.title}'


class PackageFeature(models.Model):
    title = models.CharField(_('Title'), max_length=128)
    description = RichTextField(_('Description'), blank=True, null=True)
    icon = models.ImageField(_('Icon'), upload_to='images/packages/features/')

    class Meta:
        verbose_name = _('Plan feature')
        verbose_name_plural = _('Plan features')

    def __str__(self):
        return self.title


class ActivityBridge(models.Model):
    day = models.ForeignKey('packages.Day', related_name='activities', on_delete=models.CASCADE, verbose_name=_('Day'))
    plan = models.ForeignKey('packages.Plan', related_name='activities', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('Plan'))
    activity = models.ForeignKey('packages.Activity', related_name='bridges', on_delete=models.PROTECT, verbose_name=_('Activity'))
    due_time = models.TimeField(_('Due time'))

    class Meta:
        verbose_name = _('Activity in Day')
        verbose_name_plural = _('Activities in Day')

    def __str__(self):
        return f'{self.plan.type} - {self.activity.title}'


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


class ActivityPicture(TimeStampedModel):
    activity = models.ForeignKey('packages.Activity', related_name='pictures', on_delete=models.PROTECT, verbose_name=_('Activity'))
    picture = models.ImageField(_('Picture'), upload_to='images/packages/activities/%Y/%m')

    is_main = models.BooleanField(_('Is main?'), default=False)

    class Meta:
        verbose_name = _('Activity picture')
        verbose_name_plural = _('Activity pictures')

    def save(self, *args, **kwargs):
        if self.activity.pictures.exclude(self).filter(is_main=True).exists():
            self.activity.pictures.update(is_main=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Picture for {self.activity} {self.id}'


__all__ = ['Day', 'Stay', 'Flight', 'PackageFeature', 'Activity', 'ActivityBridge', 'ActivityPicture']
