from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from apps.base.models import TimeStampedModel


class Trip(TimeStampedModel):
    package = models.ForeignKey('packages.Package', related_name='trips', on_delete=models.CASCADE, verbose_name=_('Package'))
    start_date = models.DateField(_('Start date'), default=timezone.now)
    end_date = models.DateField(_('End date'), default=timezone.now)

    class Meta:
        verbose_name = _('Trip')
        verbose_name_plural = _('Trips')

    def __str__(self):
        return self.start_date


class Package(TimeStampedModel):
    core_activities = models.ManyToManyField('packages.Activity', related_name='packages', blank=True, verbose_name=_('Core activities'))
    title = models.CharField(_('Title'), max_length=256)
    picture = models.ImageField(_('Picture'), upload_to='images/packages/packages/%Y/%m/')
    country = models.ForeignKey('accommodations.Country', related_name='packages', on_delete=models.PROTECT, verbose_name=_('Country'))
    duration = models.PositiveIntegerField(_('Duration'))
    active = models.BooleanField(_('Active status'), default=True)
    discount = models.PositiveIntegerField(_('Discount'), default=0, validators=[MaxValueValidator(100)])

    class Meta:
        verbose_name = _('Package')
        verbose_name_plural = _('Packages')

    def __str__(self):
        return self.title


class Destination(models.Model):
    package = models.ForeignKey('packages.Package', related_name='destinations', on_delete=models.CASCADE, verbose_name=_('Package'))
    city = models.ForeignKey('accommodations.City', related_name='packages', on_delete=models.PROTECT, verbose_name=_('City'))
    duration = models.PositiveIntegerField(_('Duration in days'), validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = _('Destination')
        verbose_name_plural = _('Destinations')

    def clean(self):
        if self.city not in self.package.country.cities.all():
            raise ValidationError({'city': 'Does not exist in the list of cities of the country of the package.'})

    def __str__(self):
        return f"{self.city}, {self.country} - {self.duration} {'days' if self.duration >= 2 else 'day'}"


class PlanType(models.Model):
    title = models.CharField(_('Title'), max_length=128)

    class Meta:
        verbose_name = _('Plan type')
        verbose_name_plural = _('Plan types')

    def __str__(self):
        return self.title


class Plan(models.Model):
    package = models.ForeignKey('packages.Package', related_name='plans', on_delete=models.CASCADE, verbose_name=_('Package'))
    type = models.ForeignKey('packages.PlanType', related_name='plans', on_delete=models.PROTECT, verbose_name=_('Type'))
    price = models.PositiveIntegerField(_('Price'))
    features = models.ManyToManyField('packages.PlanFeature', related_name='plans', blank=True, verbose_name=_('Features'))
    activities = models.ManyToManyField('packages.Activity', related_name='plans', blank=True, verbose_name=_('Plan-specific cctivities'))
    description = RichTextField(_('Description'), blank=True, null=True)

    class Meta:
        verbose_name = _('Plan')
        verbose_name_plural = _('Plans')

    @property
    def get_discounted_price(self):
        return self.price if self.package.discount == 0 else self.price * ((100 - self.package.discount) / 100)

    def __str__(self):
        return f'{self.package.title} - {self.type.title}'


class PlanFeature(models.Model):
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


__all__ = ['Trip', 'Package', 'PlanType', 'Plan', 'PlanFeature', 'Activity', 'Destination']
