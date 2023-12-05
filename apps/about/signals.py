from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Location, SocialMedia


@receiver(post_save, sender=Location)
@receiver(post_delete, sender=Location)
def delete_cache(sender, instance, created, **kwargs):
    cache.delete('about:locations')


@receiver(post_save, sender=SocialMedia)
@receiver(post_delete, sender=SocialMedia)
def delete_cache(sender, instance, created, **kwargs):
    cache.delete('about:social_media')
