from rest_framework.generics import ListAPIView

from apps.about.models import Location
from .serializers import LocationListSerializer


class LocationListAPIView(ListAPIView):
    serializer_class = LocationListSerializer
    queryset = Location.objects.all()


__all__ = ['LocationListAPIView']
