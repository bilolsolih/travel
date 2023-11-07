from rest_framework.serializers import ModelSerializer

from apps.places.models import PopularPlace


class PopularPlaceListSerializer(ModelSerializer):
    class Meta:
        model = PopularPlace
        fields = ['id', 'title', 'description', 'picture', 'get_count']
