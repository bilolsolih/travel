from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.models import TimeStampedModel


class Notification(TimeStampedModel):
    title = models.CharField(_('Title'), max_length=256)
    description = RichTextField(_('Description'))
    picture = models.ImageField(_('Picture'), upload_to='images/notifications/')

    class Meta:
        verbose_name = _('Notification')
        verbose_name_plural = _('Notifications')

    def __str__(self):
        return self.title
