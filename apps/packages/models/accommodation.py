from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.models import TimeStampedModel


class AccommodationType(models.Model):
    title = models.CharField(_('Title'), max_length=128)
    picture = models.ImageField(_('Picture'), upload_to='images/accommodations/accommodation_types/')

    class Meta:
        verbose_name = _('Accommodation type')
        verbose_name_plural = _('Accommodation types')

    def __str__(self):
        return self.title


class Accommodation(TimeStampedModel):
    title = models.CharField(_('Title'), max_length=128)
    type = models.ForeignKey('packages.AccommodationType', related_name='accommodations', on_delete=models.PROTECT, verbose_name=_('Type'))
    short_description = models.TextField(_('Short description'))
    long_description = RichTextField(_('Long description'))
    rating = models.DecimalField(_('Rating'), max_digits=2, decimal_places=1)
    country = models.ForeignKey('base.Country', related_name='accommodations', on_delete=models.PROTECT, blank=True, null=True, verbose_name=_('Country'))
    city = models.ForeignKey('base.City', related_name='accommodations', on_delete=models.PROTECT, blank=True, null=True, verbose_name=_('City'))
    address = models.CharField(_('Address'), max_length=256)
    landmark = models.CharField(_('Landmark'), max_length=256, blank=True, null=True)
    features = models.ManyToManyField('packages.AccommodationFeature', related_name='accommodations', blank=True)

    iframe = models.TextField(_('iFrame'), blank=True, null=True)
    embedded_link = models.TextField(_('Embedded Map link'), blank=True, null=True)
    latitude = models.CharField(_('Latitude'), max_length=64, blank=True, null=True)
    longitude = models.CharField(_('Longitude'), max_length=64, blank=True, null=True)

    class Meta:
        verbose_name = _('Accommodation')
        verbose_name_plural = _('Accommodations')

    def clean(self):
        if not self.country.cities.contains(self.city):
            raise ValidationError({'city': 'No such City in the Country.'})

    def __str__(self):
        return self.title


class AccommodationPicture(TimeStampedModel):
    accommodation = models.ForeignKey('packages.Accommodation', related_name='pictures', on_delete=models.PROTECT, verbose_name=_('Accommodation'))
    picture = models.ImageField(_('Picture'), upload_to='images/accommodations/destinations/%Y/%m/%d/')

    is_main = models.BooleanField(_('Is main?'), default=False)

    class Meta:
        verbose_name = _('Accommodation picture')
        verbose_name_plural = _('Accommodation pictures')

    def save(self, *args, **kwargs):
        if self.is_main:
            queryset = self.accommodation.pictures.exclude(pk=self.pk).filter(is_main=True)
            if queryset.exists():
                queryset.update(is_main=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Picture {self.id} for {self.accommodation}'


class AccommodationFeature(models.Model):
    title = models.CharField(_('Title'), max_length=128)
    icon = models.ImageField(_('Icon'), upload_to='images/accommodations/features/')
    description = models.TextField(_('Description'), blank=True, null=True)
    is_paid = models.BooleanField(_('Is paid?'), default=False)
    is_popular = models.BooleanField(_('Is popular?'), default=False)

    class Meta:
        verbose_name = _('Accommodation feature')
        verbose_name_plural = _('Accommodation features')

    def __str__(self):
        return self.title


__all__ = ['AccommodationType', 'Accommodation', 'AccommodationPicture', 'AccommodationFeature']
