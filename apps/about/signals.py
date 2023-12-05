from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Location, SocialMedia, FrequentlyAskedQuestion, TermsAndConditions


@receiver(post_save, sender=Location)
@receiver(post_delete, sender=Location)
def delete_cache(sender, instance, created, **kwargs):
    cache.delete('about:locations')


@receiver(post_save, sender=SocialMedia)
@receiver(post_delete, sender=SocialMedia)
def delete_cache(sender, instance, created, **kwargs):
    cache.delete('about:social_media')


@receiver(post_save, sender=FrequentlyAskedQuestion)
@receiver(post_delete, sender=FrequentlyAskedQuestion)
def delete_cache(sender, instance, created, **kwargs):
    cache.delete('about:questions')


@receiver(post_save, sender=TermsAndConditions)
@receiver(post_delete, sender=TermsAndConditions)
def delete_cache(sender, instance, created, **kwargs):
    cache.delete('about:terms')
