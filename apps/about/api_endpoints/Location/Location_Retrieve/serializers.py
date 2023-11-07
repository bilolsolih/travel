from rest_framework.serializers import ModelSerializer

from apps.about.models import Location
from apps.base.models import Region


class RegionInLocationRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'title']


class LocationRetrieveSerializer(ModelSerializer):
    region = RegionInLocationRetrieveSerializer(many=False)

    class Meta:
        model = Location
        fields = ['id', 'region', 'city', 'title', 'iframe', 'latitude', 'longitude']
