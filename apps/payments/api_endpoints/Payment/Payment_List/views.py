import django_filters
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.payments.models import Payment
from .serializers import PaymentListSerializer
from django_filters.rest_framework.backends import DjangoFilterBackend
from django_filters.filterset import FilterSet


class PaymentFilterSet(FilterSet):
    title = django_filters.CharFilter(field_name='package')

class PaymentListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentListSerializer

    def get_queryset(self):
        return Payment.objects.filter(payer=self.request.user)


__all__ = ['PaymentListAPIView']
