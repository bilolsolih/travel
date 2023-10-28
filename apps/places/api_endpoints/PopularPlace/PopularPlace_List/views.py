from rest_framework.generics import ListAPIView

from apps.places.models import PopularPlace
from .serializers import PopularPlaceListSerializer


class PopularPlaceListAPIView(ListAPIView):
    serializer_class = PopularPlaceListSerializer
    queryset = PopularPlace.objects.all()


__all__ = ['PopularPlaceListAPIView']
