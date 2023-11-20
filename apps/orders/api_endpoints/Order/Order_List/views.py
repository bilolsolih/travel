import django_filters
from django_filters.filterset import FilterSet
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.orders.models import Order
from .serializers import OrderListSerializer


class OrderFilterSet(FilterSet):
    title = django_filters.CharFilter(field_name='package__title', lookup_expr='icontains')


class OrderListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilterSet

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


__all__ = ['OrderListAPIView']
