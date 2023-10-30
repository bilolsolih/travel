import os

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.models import TimeStampedModel


class PopularPlace(TimeStampedModel):
    title = models.CharField(_('Title'), max_length=256)
    picture = models.ImageField(_('Picture'), upload_to='images/places/')
    description = models.TextField(_('Description'))

    class Meta:
        verbose_name = _('Popular place')
        verbose_name_plural = _('Popular places')

    def delete(self, *args, **kwargs):
        if os.path.exists(self.picture.path):
            os.remove(self.picture.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title


# class Picture(TimeStampedModel):
#     popular_place = models.ForeignKey('places.PopularPlace', related_name='pictures', on_delete=models.PROTECT)
#     is_main = models.BooleanField(_('Main status'), default=False)
#     picture = models.ImageField(_('Picture'), upload_to='images/places/')
#
#     class Meta:
#         verbose_name = _('Picture')
#         verbose_name_plural = _('Pictures')
#         unique_together = ['popular_place', 'is_main']
#
#     def delete(self, *args, **kwargs):
#         if os.path.exists(self.picture.path):
#             os.remove(self.picture.path)
#         super().delete(*args, **kwargs)
#
#     def __str__(self):
#         return f'{self.popular_place} - {self.id}'
