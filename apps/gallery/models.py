from django.db import models
from django.utils.translation import gettext_lazy as _


class MainPagePictures(models.Model):
    title = models.CharField(_('Title'), max_length=256, blank=True, null=True)
    picture = models.ImageField(_('Picture'), upload_to='images/gallery/main_page/')
    prompt = models.CharField(_('Text prompt'), max_length=256)

    active = models.BooleanField(_('Active status'), default=True)

    class Meta:
        verbose_name = _('Main page picture')
        verbose_name_plural = _('Main page pictures')
        indexes = [
            models.Index(fields=('active',))
        ]

    def __str__(self):
        if self.title:
            return self.title
        else:
            return f'Main page picture - {self.id}'
