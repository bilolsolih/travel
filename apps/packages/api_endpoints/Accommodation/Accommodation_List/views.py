from rest_framework.generics import ListAPIView

from apps.packages.models import Accommodation
from .serializers import AccommodationListSerializer


class AccommodationListAPIView(ListAPIView):
    serializer_class = AccommodationListSerializer

    def get_queryset(self):
        return Accommodation.objects.all()


__all__ = ['AccommodationListAPIView']
