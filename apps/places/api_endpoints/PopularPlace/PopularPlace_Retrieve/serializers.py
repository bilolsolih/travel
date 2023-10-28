from rest_framework.serializers import ModelSerializer

from apps.places.models import PopularPlace, Picture


class PictureInPopularPlaceRetrieve(ModelSerializer):
    class Meta:
        model = Picture
        fields = ['id', 'picture', 'is_main']


class PopularPlaceRetrieveSerializer(ModelSerializer):
    pictures = PictureInPopularPlaceRetrieve(many=True)

    class Meta:
        model = PopularPlace
        fields = ['id', 'title', 'pictures']
