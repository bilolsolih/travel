from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.payments.models import Payment
from .serializers import PaymentListSerializer


class PaymentListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentListSerializer

    def get_queryset(self):
        return Payment.objects.filter(payer=self.request.user)


__all__ = ['PaymentListAPIView']
