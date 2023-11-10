from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Package


@receiver(post_save, sender=Package)
@receiver(post_delete, sender=Package)
def delete_cache(sender, instance, created, **kwargs):
    cache.delete('all_packages')
