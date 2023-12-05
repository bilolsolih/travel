from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.core.cache import cache
from apps.discounts.models import Discount
from apps.packages.models import Package
from .serializers import DiscountListSerializer


class DiscountListAPIView(ListAPIView):
    serializer_class = DiscountListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        packages_length = Package.objects.filter(discounts__isnull=True).count()
        return Response({'discount_companies': serializer.data, 'packages_length': packages_length})

    def get_queryset(self):
        queryset = cache.get('discounts:discount')
        if not queryset:
            queryset = Discount.objects.filter(is_active=True)
            cache.set('discounts:discount', queryset, timeout=60 * 60 * 6)
        return queryset


__all__ = ['DiscountListAPIView']
