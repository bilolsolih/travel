from rest_framework import serializers

from apps.accounts.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password_check = serializers.CharField(write_only=True, min_length=8, max_length=32)

    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'phone_number', 'email', 'password', 'password_check']

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)

    def validate(self, attrs):
        if attrs['password'] != attrs['password_check']:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})
        del attrs['password_check']
        return attrs
