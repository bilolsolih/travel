from rest_framework.generics import RetrieveAPIView

from apps.places.models import PopularPlace
from .serializers import PopularPlaceRetrieveSerializer


class PopularPlaceRetrieveAPIView(RetrieveAPIView):
    serializer_class = PopularPlaceRetrieveSerializer
    queryset = PopularPlace.objects.all()


__all__ = ['PopularPlaceRetrieveAPIView']
