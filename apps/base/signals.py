from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import City, Country, Region


@receiver(post_save, sender=City)
@receiver(post_delete, sender=City)
def delete_cache(sender, instance, created, **kwargs):
    cache.delete('base:city')


@receiver(post_save, sender=Country)
@receiver(post_delete, sender=Country)
def delete_cache(sender, instance, created, **kwargs):
    cache.delete('base:country')


@receiver(post_save, sender=Region)
@receiver(post_delete, sender=Region)
def delete_cache(sender, instance, created, **kwargs):
    cache.delete('base:region')
