from fcm_django.models import FCMDevice
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import NotificationTurnOffSerializer


class NotificationTurnOffAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationTurnOffSerializer

    def get_queryset(self):
        queryset = FCMDevice.objects.filter(user=self.request.user)
        return queryset


__all__ = ['NotificationTurnOffAPIView']
