from rest_framework.generics import ListAPIView

from apps.gallery.models import MainPagePictures
from .serializers import MainPagePictureListSerializer


class MainPagePictureListAPIView(ListAPIView):
    serializer_class = MainPagePictureListSerializer
    queryset = MainPagePictures.objects.filter(active=True)


__all__ = ['MainPagePictureListAPIView']
