from rest_framework.generics import ListAPIView
from django.core.cache import cache
from apps.about.models import Location
from .serializers import LocationListSerializer


class LocationListAPIView(ListAPIView):
    serializer_class = LocationListSerializer

    def get_queryset(self):
        queryset = cache.get('about:locations')
        if not queryset:
            queryset = Location.objects.all().select_related('region')
            cache.set('about:locations', queryset, timeout=60 * 60 * 6)
        return queryset


__all__ = ['LocationListAPIView']
