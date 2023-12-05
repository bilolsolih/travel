from django.core.cache import cache
from rest_framework.generics import ListAPIView

from apps.base.models import City
from .serializers import CityListSerializer


class CityListAPIView(ListAPIView):
    serializer_class = CityListSerializer

    def get_queryset(self):
        queryset = cache.get('base:city')
        if not queryset:
            queryset = City.objects.all()
            cache.set('base:city', queryset, timeout=60 * 60 * 6)
        return queryset


__all__ = ['CityListAPIView']
