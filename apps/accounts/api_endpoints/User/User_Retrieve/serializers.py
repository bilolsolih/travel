from rest_framework.serializers import ModelSerializer

from apps.accounts.models import User


class UserRetrieveSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'gender', 'birthdate', 'phone_number', 'email']
