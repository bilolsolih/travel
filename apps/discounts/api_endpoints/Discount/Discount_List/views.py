from django.utils import timezone
from rest_framework.generics import ListAPIView

from apps.discounts.models import Discount
from apps.packages.models import Package
from .serializers import DiscountListSerializer
from rest_framework.response import Response


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
        return Response(serializer.data, {'packages_length': packages_length})

    def get_queryset(self):
        return Discount.objects.filter(expiry_date__gt=timezone.now())


__all__ = ['DiscountListAPIView']
