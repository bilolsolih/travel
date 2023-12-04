from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.models import TimeStampedModel


class FCMToken(TimeStampedModel):
    user = models.ForeignKey('accounts.User', related_name='fcm_tokens', on_delete=models.CASCADE, verbose_name=_('User'))
    token = models.CharField(_('FCM Token'), max_length=256)
    will_receive = models.BooleanField(_('Will receive?'), default=True)

    class Meta:
        verbose_name = _('FCM token')
        verbose_name_plural = _('FCM tokens')

    def __str__(self):
        return f"{self.user.phone_number} - {self.token}"
