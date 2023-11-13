from rest_framework.serializers import ModelSerializer

from apps.base.models import Country


class CountryListSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'title']
