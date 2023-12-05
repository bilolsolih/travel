from django.core.cache import cache
from rest_framework.generics import ListAPIView

from apps.base.models import Country
from .serializers import CountryListSerializer


class CountryListAPIView(ListAPIView):
    serializer_class = CountryListSerializer

    def get_queryset(self):
        queryset = cache.get('base:country')
        if not queryset:
            queryset = Country.objects.all()
            cache.set('base:country', queryset, timeout=60 * 60 * 6)
        return queryset


__all__ = ['CountryListAPIView']
