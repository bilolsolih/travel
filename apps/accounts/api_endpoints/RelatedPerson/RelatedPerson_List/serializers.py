from rest_framework.serializers import ModelSerializer

from apps.accounts.models import RelatedPerson


class RelatedPersonListSerializer(ModelSerializer):
    class Meta:
        model = RelatedPerson
        fields = ['phone_number', 'first_name', 'last_name']
