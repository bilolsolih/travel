from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import FCMTokenCreateSerializer


class FCMTokenCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FCMTokenCreateSerializer


__all__ = ['FCMTokenCreateAPIView']
