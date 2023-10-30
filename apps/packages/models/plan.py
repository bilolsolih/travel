from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


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
    price = models.PositiveIntegerField(_('Price in USD ($)'))
    discount = models.PositiveIntegerField(_('Discount'), validators=[MaxValueValidator(100)])
    discount_expiry_date = models.DateTimeField(_('Discount expiry date'), blank=True, null=True)
    features = models.ManyToManyField('packages.PackageFeature', related_name='plans', blank=True, verbose_name=_('Features'))
    description = RichTextField(_('Description'), blank=True, null=True)

    class Meta:
        verbose_name = _('Plan')
        verbose_name_plural = _('Plans')
        unique_together = ['package', 'type']

    @property
    def get_discounted_price(self):
        if self.discount and self.discount_expiry_date and self.discount_expiry_date > timezone.now():
            return self.price * ((100 - self.discount) / 100)
        else:
            return self.price

    def clean(self):
        if self.discount and not self.discount_expiry_date:
            raise ValidationError({'discount_expiry_date': 'When discount is set, this field also must be set.'})

    def __str__(self):
        return f'{self.package.title} - {self.type.title}'


__all__ = ['PlanType', 'Plan']
