from rest_framework import serializers


class NotificationSendSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()
    image = serializers.URLField()
