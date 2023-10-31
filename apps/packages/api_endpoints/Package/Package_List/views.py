import django_filters
from django_filters.rest_framework.backends import DjangoFilterBackend
from django_filters.rest_framework.filterset import FilterSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.packages.models import Package
from apps.places.models import PopularPlace
from .serializers import PackageListSerializer


class PackageFilterSet(FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    popular_places = django_filters.ModelChoiceFilter(field_name='popular_places', to_field_name='id', queryset=PopularPlace.objects.all())


class PackageListAPIView(ListAPIView):
    serializer_class = PackageListSerializer
    queryset = Package.objects.filter(is_active=True)
    filter_backends = [DjangoFilterBackend]
    filterset_class = PackageFilterSet


class PackageLikedListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PackageListSerializer

    def get_queryset(self):
        return self.request.user.liked_packages.all()


__all__ = ['PackageListAPIView', 'PackageLikedListAPIView']
