from rest_framework.serializers import ModelSerializer

from apps.gallery.models import MainPagePictures


class MainPagePictureListSerializer(ModelSerializer):
    class Meta:
        model = MainPagePictures
        fields = ['id', 'title', 'picture', 'prompt']
