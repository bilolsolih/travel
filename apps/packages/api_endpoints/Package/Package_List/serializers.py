from rest_framework.serializers import ModelSerializer

from apps.packages.models import Package


class PackageListSerializer(ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'title', 'picture', 'country', 'city', 'duration']
