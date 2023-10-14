from rest_framework.serializers import ModelSerializer

from apps.accounts.models import User


class UserRetrieveSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'phone_number', 'email', 'is_verified', 'first_name', 'last_name', 'middle_name', 'gender', 'birthdate',
            'passport_picture', 'individual_pin', 'serial_number', 'region', 'district', 'balance'
        ]
