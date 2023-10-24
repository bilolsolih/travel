from rest_framework import serializers

from apps.accounts.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'region', 'profile_photo']

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)
