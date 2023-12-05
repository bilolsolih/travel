from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Discount


@receiver(signal=post_save, sender=Discount)
@receiver(signal=post_delete, sender=Discount)
def delete_cache(sender, instance, created, **kwargs):
    cache.delete('discounts:discount')
