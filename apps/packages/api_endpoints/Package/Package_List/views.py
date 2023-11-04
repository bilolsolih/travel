import django_filters
from django_filters.rest_framework.backends import DjangoFilterBackend
from django_filters.rest_framework.filterset import FilterSet
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from apps.packages.models import Package
from apps.places.models import PopularPlace
from .serializers import PackageListSerializer


class PackageFilterSet(FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    popular_places = django_filters.ModelChoiceFilter(field_name='popular_places', to_field_name='id', queryset=PopularPlace.objects.all())


class CustomLimitOffsetPagination(LimitOffsetPagination):
    def get_next_link(self):
        if self.get_offset(self.request) is None:
            return None
        next_offset = self.get_offset(self.request) + self.get_limit(self.request)
        return next_offset


class PackageListAPIView(ListAPIView):
    serializer_class = PackageListSerializer
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = PackageFilterSet

    def get_queryset(self):
        queryset = Package.objects.filter(is_active=True)
        discount = self.request.query_params.get('discount', None)
        if discount:
            if discount == 0:
                queryset = queryset.fitlter(discounts__isnull=True)
            else:
                queryset = queryset.filter(discounts__pk=discount).distinct()
        return queryset

    def get(self, request, *args, **kwargs):
        if request.query_params.get('nopage', None):
            self.pagination_class = None
        return self.list(request, *args, **kwargs)


class PackageLikedListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PackageListSerializer

    def get_queryset(self):
        return self.request.user.liked_packages.all()


__all__ = ['PackageListAPIView', 'PackageLikedListAPIView']
