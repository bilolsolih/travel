from rest_framework.serializers import ModelSerializer

from apps.base.models import City
from apps.packages.models import Accommodation, AccommodationType, AccommodationFeature, AccommodationPicture


class CityInAccommodationRetrieveSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'title']


class AccommodationTypeInAccommodationRetrieveSerializer(ModelSerializer):
    class Meta:
        model = AccommodationType
        fields = ['title', 'picture']


class AccommodationPictureInAccommodationList(ModelSerializer):
    class Meta:
        model = AccommodationPicture
        fields = ['id', 'picture', 'is_main']


class AccommodationFeatureInAccommodationList(ModelSerializer):
    class Meta:
        model = AccommodationFeature
        fields = ['id', 'title', 'icon', 'description', 'is_paid', 'is_popular']


class AccommodationRetrieveSerializer(ModelSerializer):
    type = AccommodationTypeInAccommodationRetrieveSerializer(many=False)
    city = CityInAccommodationRetrieveSerializer(many=False)
    features = AccommodationFeatureInAccommodationList(many=True)
    pictures = AccommodationPictureInAccommodationList(many=True)

    class Meta:
        model = Accommodation
        fields = [
            'id', 'title', 'type', 'long_description', 'rating', 'city', 'address', 'landmark', 'features', 'iframe', 'latitude', 'longitude', 'pictures', 'embedded_link'
        ]
