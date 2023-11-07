from rest_framework.serializers import ModelSerializer

from apps.places.models import PopularPlace, Feature


class FeatureInPopularPlaceRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Feature
        fields = ['title']


class PopularPlaceRetrieveSerializer(ModelSerializer):
    features = FeatureInPopularPlaceRetrieveSerializer(many=True)

    class Meta:
        model = PopularPlace
        fields = ['id', 'title', 'description', 'picture', 'features']
