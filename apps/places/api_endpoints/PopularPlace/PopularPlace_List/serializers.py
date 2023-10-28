from rest_framework.serializers import ModelSerializer

from apps.places.models import PopularPlace, Picture


class PictureInPopularPlaceList(ModelSerializer):
    class Meta:
        model = Picture
        fields = ['picture']


class PopularPlaceListSerializer(ModelSerializer):
    get_main_picture = PictureInPopularPlaceList(many=False)

    class Meta:
        model = PopularPlace
        fields = ['id', 'title', 'get_main_picture']
