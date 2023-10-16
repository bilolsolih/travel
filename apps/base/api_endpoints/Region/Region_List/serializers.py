from rest_framework.serializers import ModelSerializer

from apps.base.models import Region


class RegionListSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = ['title']
