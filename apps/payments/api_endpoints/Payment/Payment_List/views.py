import django_filters
from django_filters.filterset import FilterSet
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.payments.models import Payment
from .serializers import PaymentListSerializer


class PaymentFilterSet(FilterSet):
    title = django_filters.CharFilter(field_name='order__package__title', lookup_expr='icontains')


class PaymentListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentFilterSet

    def get_queryset(self):
        return Payment.objects.filter(payer=self.request.user)


__all__ = ['PaymentListAPIView']
