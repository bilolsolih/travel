from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.models import TimeStampedModel


class Category(models.Model):
    title = models.CharField(_('Title'), max_length=128)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class PaymentStatus(models.TextChoices):
    WAITING = ('waiting', _('Waiting for verification'))
    VERIFIED = ('verified', _('Verified'))
    CANCELED = ('canceled', _('Canceled'))


class Payment(TimeStampedModel):
    category = models.ForeignKey('payments.Category', related_name='payments', on_delete=models.PROTECT, verbose_name=_('Payment category'))
    order = models.ForeignKey('orders.Order', related_name='payments', on_delete=models.SET_NULL, null=True, verbose_name=_('Order'))
    payer = models.ForeignKey('accounts.User', related_name='payments', on_delete=models.SET_NULL, null=True, verbose_name=_('Payer'))
    payee = models.ForeignKey('accounts.User', related_name='receivements', on_delete=models.SET_NULL, null=True, verbose_name=_('Payee'))
    responsible = models.ForeignKey('accounts.User', related_name='responsible_payments', on_delete=models.SET_NULL, null=True, verbose_name=_('Responsible person'))
    description = models.TextField(_('Description'))
    amount = models.PositiveIntegerField(_('Amount'))

    status = models.CharField(_('Status'), max_length=10, choices=PaymentStatus.choices, default=PaymentStatus.WAITING)

    class Meta:
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')

    def __str__(self):
        return f'Payment by {self.payer} to {self.payee}'

# Create your models here.
