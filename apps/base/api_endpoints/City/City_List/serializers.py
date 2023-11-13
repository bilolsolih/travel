from rest_framework.serializers import ModelSerializer

from apps.base.models import City


class CityListSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'title']
