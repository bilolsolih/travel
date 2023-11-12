import django_filters
from rest_framework.generics import ListAPIView

from apps.base.models import Country
from apps.packages.models import Accommodation
from .serializers import AccommodationListSerializer


class AccommodationFilterSet(django_filters.FilterSet):
    country = django_filters.ModelChoiceFilter(field_name='country', queryset=Country.objects.all(), to_field_name='pk')


class AccommodationListAPIView(ListAPIView):
    serializer_class = AccommodationListSerializer
    filter_backends = [django_filters.rest_framework.backends.DjangoFilterBackend]
    filterset_class = AccommodationFilterSet

    def get_queryset(self):
        return Accommodation.objects.all()


__all__ = ['AccommodationListAPIView']
