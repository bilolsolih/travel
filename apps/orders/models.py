from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from apps.base.models import TimeStampedModel


class OrderStatus(models.TextChoices):
    WAITING = ('waiting', _('Waiting for payment'))
    PAID = ('paid', _('Paid'))
    COMPLETED = ('completed', _('Completed'))
    CANCELED = ('canceled', _('Canceled'))


class Order(TimeStampedModel):
    user = models.ForeignKey('accounts.User', related_name='orders', on_delete=models.PROTECT, verbose_name=_('User'))
    package = models.ForeignKey('packages.Package', related_name='orders', on_delete=models.CASCADE, verbose_name=_('Package'))
    trip = models.ForeignKey('packages.Trip', related_name='orders', on_delete=models.SET_NULL, null=True, verbose_name=_('Trip'))
    plan = models.ForeignKey('packages.Plan', related_name='orders', on_delete=models.SET_NULL, null=True, verbose_name=_('Plan'))
    price_total = models.PositiveIntegerField(_('Total price'))
    price_paid = models.PositiveIntegerField(_('Price paid'), default=0)

    status = models.CharField(_('Status'), choices=OrderStatus.choices, max_length=10, default=OrderStatus.WAITING)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def clean(self):
        if not self.package.trips.contains(self.trip):
            raise ValidationError({'trip': _('No such Trip in the Package.')})
        if not self.package.plans.contains(self.plan):
            raise ValidationError({'plan': _('No such Plan in the Package.')})

    @property
    def get_price_to_pay(self):
        return self.price_total - self.price_paid

    def __str__(self):
        return f'Order by {self.user.first_name} for {self.package.title}'
