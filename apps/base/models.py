from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    created = models.DateTimeField(_('Date created'), auto_now_add=True)
    updated = models.DateTimeField(_('Date updated'), auto_now=True)

    class Meta:
        abstract = True

