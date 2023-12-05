from django.core.cache import cache
from rest_framework.generics import ListAPIView

from apps.about.models import SocialMedia
from .serializers import SocialMediaListSerializer


class SocialMediaListAPIView(ListAPIView):
    serializer_class = SocialMediaListSerializer
    queryset = SocialMedia.objects.all()

    def get_queryset(self):
        queryset = cache.get('about:social_media')
        if not queryset:
            queryset = SocialMedia.objects.all()
            cache.set('about:social_media', queryset, timeout=60 * 60 * 6)
        return queryset


__all__ = ['SocialMediaListAPIView']
