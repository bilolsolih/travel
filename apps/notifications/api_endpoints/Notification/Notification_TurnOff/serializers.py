from rest_framework.serializers import ModelSerializer

from fcm_django.models import FCMDevice


class NotificationTurnOffSerializer(ModelSerializer):
    class Meta:
        model = FCMDevice
        fields = ['active']
