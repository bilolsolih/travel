from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.payments.models import Payment
from .serializers import PaymentRetrieveSerializer


class PaymentRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentRetrieveSerializer

    def get_queryset(self):
        return Payment.objects.filter(payer=self.request.user)


__all__ = ['PaymentRetrieveAPIView']
