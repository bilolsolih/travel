from rest_framework.generics import ListAPIView

from apps.base.models import Country
from .serializers import CountryListSerializer


class CountryListAPIView(ListAPIView):
    serializer_class = CountryListSerializer
    queryset = Country.objects.all()


__all__ = ['CountryListAPIView']
