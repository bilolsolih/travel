from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import OrderCreateSerializer


class OrderCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderCreateSerializer


__all__ = ['OrderCreateAPIView']
