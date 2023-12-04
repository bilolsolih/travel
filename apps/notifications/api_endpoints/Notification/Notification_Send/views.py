from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import NotificationSendSerializer


class NotificationSendAPIView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = NotificationSendSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        notification = Notification(title=data['title'], body=data['body'], image=data['image'])
        message = Message(notification=notification)
        devices = FCMDevice.objects.filter(active=True)
        devices.send_message(message)
        return Response(status=status.HTTP_200_OK)
