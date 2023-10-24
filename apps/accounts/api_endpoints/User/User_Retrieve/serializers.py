from rest_framework.serializers import ModelSerializer

from apps.accounts.models import User


class UserRetrieveSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'phone_number', 'is_verified', 'first_name', 'last_name', 'gender', 'birthdate', 'profile_photo',
            'passport_picture', 'individual_pin', 'serial_number', 'region', 'district', 'balance'
        ]
