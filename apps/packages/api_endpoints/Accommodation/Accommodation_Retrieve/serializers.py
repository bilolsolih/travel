from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.base.models import Country
from apps.packages.models import Accommodation, AccommodationType, AccommodationFeature, AccommodationPicture


class CountryInAccommodationRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'title']


class CityInAccommodationRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Country
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
    country = CountryInAccommodationRetrieveSerializer(many=False)
    city = CityInAccommodationRetrieveSerializer(many=False)
    features = AccommodationFeatureInAccommodationList(many=True)
    pictures = AccommodationPictureInAccommodationList(many=True)

    class Meta:
        model = Accommodation
        fields = [
            'id', 'title', 'type', 'long_description', 'rating', 'country', 'city', 'address', 'landmark', 'features', 'iframe', 'latitude', 'longitude', 'pictures', 'embedded_link'
        ]
