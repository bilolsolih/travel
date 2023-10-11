from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField(min_length=8, max_length=32)
