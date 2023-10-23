from rest_framework.serializers import ModelSerializer

from apps.accounts.models import RelatedPerson


class RelatedPersonCreateSerializer(ModelSerializer):
    class Meta:
        model = RelatedPerson
        fields = [
            'phone_number', 'is_phone_number_same', 'email', 'first_name', 'last_name', 'gender', 'birthdate',
            'passport_picture', 'individual_pin', 'serial_number', 'region', 'district', 'is_address_same'
        ]
