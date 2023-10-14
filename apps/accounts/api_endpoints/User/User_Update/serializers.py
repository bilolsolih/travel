from rest_framework.serializers import ModelSerializer

from apps.accounts.models import User


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email', 'first_name', 'last_name', 'middle_name', 'gender', 'birthdate',
            'passport_picture', 'individual_pin', 'serial_number', 'region', 'district',
        ]
