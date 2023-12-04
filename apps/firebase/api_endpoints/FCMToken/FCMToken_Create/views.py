from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import FCMTokenCreateSerializer


class FCMTokenCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FCMTokenCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


__all__ = ['FCMTokenCreateAPIView']
