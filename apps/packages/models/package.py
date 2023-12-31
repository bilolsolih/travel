import os

# from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.base.models import TimeStampedModel


class Package(TimeStampedModel):
    title = models.CharField(_('Title'), max_length=256)
    description = models.TextField(_('Description'), blank=True, null=True)
    popular_places = models.ManyToManyField('places.PopularPlace', related_name='packages', blank=True, verbose_name=_('Popular places'))
    country = models.ForeignKey('base.Country', related_name='packages', on_delete=models.PROTECT, verbose_name=_('Country'), null=True)
    duration = models.PositiveIntegerField(_('Duration'), default=1)

    flight_from = models.ForeignKey('base.Region', related_name='trips', on_delete=models.PROTECT, verbose_name=_('Region'), null=True)
    start_date = models.DateField(_('Start date'), default=timezone.now)
    end_date = models.DateField(_('End date'), default=timezone.now)

    core_features = models.ManyToManyField('packages.PackageFeature', related_name='packages', blank=True, verbose_name=_('Core features'))

    is_active = models.BooleanField(_('Active status'), default=True)

    class Meta:
        verbose_name = _('Package')
        verbose_name_plural = _('Packages')
        ordering = ('start_date',)
        indexes = [
            models.Index(fields=('title',)),
            models.Index(fields=('is_active',)),
        ]

    def __str__(self):
        return self.title


class PackagePicture(TimeStampedModel):
    package = models.ForeignKey('packages.Package', related_name='pictures', on_delete=models.PROTECT, verbose_name=_('Package'))
    picture = models.ImageField(_('Picture'), upload_to='images/packages/package/%Y/%m/')
    is_main = models.BooleanField(_('Is main?'), default=False)

    class Meta:
        verbose_name = _('Package picture')
        verbose_name_plural = _('Package pictures')

    def save(self, *args, **kwargs):
        if self.is_main:
            queryset = self.package.pictures.exclude(pk=self.pk).filter(is_main=True)
            if queryset.exists():
                queryset.update(is_main=False)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if os.path.exists(self.picture.path):
            os.remove(self.picture.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f'Picture {self.id} for {self.package}'


class Destination(models.Model):
    package = models.ForeignKey('packages.Package', related_name='destinations', on_delete=models.CASCADE, verbose_name=_('Package'))
    city = models.ForeignKey('base.City', related_name='packages', on_delete=models.PROTECT, verbose_name=_('City'))
    duration = models.PositiveIntegerField(_('Duration in days'), validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = _('Destination')
        verbose_name_plural = _('Destinations')

    def __str__(self):
        return f"{self.city} - {self.duration} {'days' if self.duration >= 2 else 'day'}"


__all__ = ['Package', 'PackagePicture', 'Destination']
