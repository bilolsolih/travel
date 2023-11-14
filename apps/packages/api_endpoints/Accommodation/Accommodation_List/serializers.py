from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.base.models import Country
from apps.packages.models import Accommodation, AccommodationType


class CountryInAccommodationListSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'title']


class CityInAccommodationListSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'title']


class AccommodationTypeInAccommodationListSerializer(ModelSerializer):
    class Meta:
        model = AccommodationType
        fields = ['title', 'picture']


class AccommodationListSerializer(ModelSerializer):
    type = AccommodationTypeInAccommodationListSerializer(many=False)
    picture = SerializerMethodField()
    country = CountryInAccommodationListSerializer(many=False)
    city = CityInAccommodationListSerializer(many=False)

    class Meta:
        model = Accommodation
        fields = ['id', 'title', 'type', 'short_description', 'rating', 'picture', 'country', 'city']

    def get_picture(self, instance):
        request = self.context['request']
        pictures = instance.pictures.all()
        if pictures.exists():
            if pictures.filter(is_main=True).exists:
                url = pictures.filter(is_main=True).first().picture.url
            else:
                url = pictures.first().picture.url
            return request.build_absolute_uri(url)
        else:
            return None
