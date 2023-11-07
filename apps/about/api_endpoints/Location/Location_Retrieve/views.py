from rest_framework.generics import RetrieveAPIView

from apps.about.models import Location
from .serializers import LocationRetrieveSerializer


class LocationRetrieveAPIView(RetrieveAPIView):
    serializer_class = LocationRetrieveSerializer
    queryset = Location.objects.all()


__all__ = ['LocationRetrieveAPIView']
