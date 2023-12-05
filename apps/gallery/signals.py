from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import MainPagePictures


@receiver(signal=post_save, sender=MainPagePictures)
@receiver(signal=post_delete, sender=MainPagePictures)
def delete_cache(sender, instance, created, **kwargs):
    cache.delete('gallery:pictures')
