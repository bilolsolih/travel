from rest_framework.serializers import ModelSerializer

from apps.places.models import PopularPlace, Feature


class FeatureInPopularPlaceListSerializer(ModelSerializer):
    class Meta:
        model = Feature
        fields = ['title']


class PopularPlaceListSerializer(ModelSerializer):
    features = FeatureInPopularPlaceListSerializer

    class Meta:
        model = PopularPlace
        fields = ['id', 'title', 'description', 'picture', 'features']
