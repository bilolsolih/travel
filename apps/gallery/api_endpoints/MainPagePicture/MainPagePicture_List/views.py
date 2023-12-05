from django.core.cache import cache
from rest_framework.generics import ListAPIView

from apps.gallery.models import MainPagePictures
from .serializers import MainPagePictureListSerializer


class MainPagePictureListAPIView(ListAPIView):
    serializer_class = MainPagePictureListSerializer

    def get_queryset(self):
        queryset = cache.get('gallery:pictures')
        if not queryset:
            queryset = MainPagePictures.objects.filter(is_active=True)
            cache.set('gallery:pictures', queryset, timeout=60 * 60 * 6)
        return queryset


__all__ = ['MainPagePictureListAPIView']
