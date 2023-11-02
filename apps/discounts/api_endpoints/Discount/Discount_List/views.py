from django.utils import timezone
from rest_framework.generics import ListAPIView

from apps.discounts.models import Discount
from .serializers import DiscountListSerializer


class DiscountListAPIView(ListAPIView):
    serializer_class = DiscountListSerializer

    def get_queryset(self):
        return Discount.objects.filter(expiry_date__gt=timezone.now())


__all__ = ['DiscountListAPIView']
