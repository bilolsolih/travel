from rest_framework.serializers import ModelSerializer

from apps.accounts.models import User


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'middle_name', 'gender', 'birthdate', 'phone_number', 'email']
