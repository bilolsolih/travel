from rest_framework.serializers import ModelSerializer

from apps.about.models import TermsAndConditions


class TermsAndConditionsRetrieveSerializer(ModelSerializer):
    class Meta:
        model = TermsAndConditions
        fields = ['terms']
