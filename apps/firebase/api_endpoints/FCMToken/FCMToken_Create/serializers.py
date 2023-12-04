from rest_framework.serializers import ModelSerializer

from apps.firebase.models import FCMToken


class FCMTokenCreateSerializer(ModelSerializer):
    class Meta:
        model = FCMToken
        fields = ['token']
