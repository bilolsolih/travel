from rest_framework.serializers import ModelSerializer

from apps.accommodations.models import Accommodation


class AccommodationListSerializer(ModelSerializer):
    class Meta:
        model = Accommodation
        fields = ['id', 'title', 'type', 'country', 'city', 'address', 'landmark', 'features', 'iframe', 'latitude', 'longitude']
