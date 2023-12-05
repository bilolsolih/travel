from django.core.cache import cache
from rest_framework.generics import ListAPIView

from apps.base.models import Region
from .serializers import RegionListSerializer


class RegionListAPIView(ListAPIView):
    serializer_class = RegionListSerializer

    def get_queryset(self):
        queryset = cache.get('base:region')
        if not queryset:
            queryset = Region.objects.all()
            cache.set('base:region', queryset, timeout=60 * 60 * 6)
        return queryset


__all__ = ['RegionListAPIView']
