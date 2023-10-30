from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.models import TimeStampedModel


class Accommodation(TimeStampedModel):
    title = models.CharField(_('Title'), max_length=128)
    type = models.ForeignKey('accommodations.AccommodationType', related_name='accommodations', on_delete=models.PROTECT, verbose_name=_('Type'))
    country = models.ForeignKey('base.Country', related_name='accommodations', on_delete=models.PROTECT, verbose_name=_('Country'))
    city = models.ForeignKey('base.City', related_name='accommodations', on_delete=models.PROTECT, verbose_name=_('City'))
    address = models.CharField(_('Address'), max_length=256)
    landmark = models.CharField(_('Landmark'), max_length=256, blank=True, null=True)
    features = models.ManyToManyField('accommodations.AccommodationFeature', related_name='accommodations', blank=True)

    iframe = models.TextField(_('iFrame'), blank=True, null=True)
    latitude = models.CharField(_('Latitude'), max_length=64, blank=True, null=True)
    longitude = models.CharField(_('Longitude'), max_length=64, blank=True, null=True)

    class Meta:
        verbose_name = _('Accommodation')
        verbose_name_plural = _('Accommodations')

    def __str__(self):
        return self.title


class AccommodationType(models.Model):
    title = models.CharField(_('Title'), max_length=128)
    picture = models.ImageField(_('Picture'), upload_to='images/accommodations/accommodation_types/')

    class Meta:
        verbose_name = _('Accommodation type')
        verbose_name_plural = _('Accommodation types')

    def __str__(self):
        return self.title


class AccommodationPicture(TimeStampedModel):
    accommodation = models.ForeignKey('accommodations.Accommodation', related_name='pictures', on_delete=models.PROTECT, verbose_name=_('Accommodation'))
    picture = models.ImageField(_('Picture'), upload_to='images/accommodations/destinations/%Y/%m/%d/')

    class Meta:
        verbose_name = _('Accommodation type')
        verbose_name_plural = _('Accommodation types')

    def __str__(self):
        return f'Picture {self.id} for {self.accommodation}'


class AccommodationFeature(models.Model):
    title = models.CharField(_('Title'), max_length=128)
    icon = models.ImageField(_('Icon'), upload_to='images/accommodations/features/')
    description = models.TextField(_('Description'), blank=True, null=True)
    is_paid = models.BooleanField(_('Is paid?'), default=False)

    class Meta:
        verbose_name = _('Feature')
        verbose_name_plural = _('Features')

    def __str__(self):
        return self.title


__all__ = ['AccommodationType', 'Accommodation', 'AccommodationPicture', 'AccommodationFeature']
