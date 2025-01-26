from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField(min_length=4, max_length=32)
