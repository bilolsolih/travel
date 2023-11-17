from rest_framework.generics import RetrieveAPIView

from apps.packages.models import Accommodation
from .serializers import AccommodationRetrieveSerializer


class AccommodationRetrieveAPIView(RetrieveAPIView):
    serializer_class = AccommodationRetrieveSerializer

    def get_queryset(self):
        return Accommodation.objects.all()


__all__ = ['AccommodationRetrieveAPIView']
