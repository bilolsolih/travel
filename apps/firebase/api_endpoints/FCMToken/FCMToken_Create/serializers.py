from rest_framework.serializers import ModelSerializer

from fcm_django.models import FCMDevice


class FCMTokenCreateSerializer(ModelSerializer):
    class Meta:
        model = FCMDevice
        fields = ['registration_id']
