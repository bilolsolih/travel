from rest_framework.serializers import ModelSerializer

from apps.about.models import Location
from apps.base.models import Region


class RegionInLocationListSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'title']


class LocationListSerializer(ModelSerializer):
    region = RegionInLocationListSerializer(many=False)

    class Meta:
        model = Location
        fields = ['id', 'region', 'city']
