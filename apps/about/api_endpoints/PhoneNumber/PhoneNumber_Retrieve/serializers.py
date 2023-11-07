from rest_framework.serializers import ModelSerializer

from apps.about.models import PhoneNumber


class PhoneNumberRetrieveSerializer(ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['phone_number']
