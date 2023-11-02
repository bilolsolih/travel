from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.models import TimeStampedModel


class Discount(TimeStampedModel):
    title = models.CharField(_('Title'), max_length=256)
    description = models.TextField(_('Description'), blank=True, null=True)
    max_discount = models.PositiveIntegerField(_('Maximum amount of discount'))
    expiry_date = models.DateTimeField(_('Expiry date'))
    packages = models.ManyToManyField('packages.Package', related_name='discounts', verbose_name=_('Packages'))

    class Meta:
        verbose_name = _('Discount')
        verbose_name_plural = _('Discounts')

    def __str__(self):
        return self.title
