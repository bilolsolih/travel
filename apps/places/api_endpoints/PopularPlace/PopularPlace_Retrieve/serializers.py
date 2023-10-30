from rest_framework.serializers import ModelSerializer

from apps.places.models import PopularPlace


class PopularPlaceRetrieveSerializer(ModelSerializer):
    class Meta:
        model = PopularPlace
        fields = ['id', 'title', 'description', 'picture']
