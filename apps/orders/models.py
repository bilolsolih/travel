from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.models import TimeStampedModel


class Order(TimeStampedModel):
    user = models.ForeignKey('accounts.User', related_name='orders', on_delete=models.PROTECT, verbose_name=_('User'))
    package = models.ForeignKey('travels.Package', related_name='orders', on_delete=models.CASCADE, verbose_name=_('Package'))
    plan = models.ForeignKey('travels.Plan', related_name='orders', on_delete=models.SET_NULL, null=True, verbose_name=_('Plan'))
    price_total = models.PositiveIntegerField(_('Total price'))
    price_paid = models.PositiveIntegerField(_('Price paid'), default=0)
    price_to_pay = models.PositiveIntegerField(_('Price to pay'))
    
    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return f'Order by {self.user.first_name} for {self.package.title}'
