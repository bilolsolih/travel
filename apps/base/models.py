from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    created = models.DateTimeField(_('Date created'), auto_now_add=True)
    updated = models.DateTimeField(_('Date updated'), auto_now=True)

    class Meta:
        abstract = True


class Region(models.Model):
    title = models.CharField(_('Title'), max_length=64, unique=True)

    class Meta:
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')

    def __str__(self):
        return self.title
