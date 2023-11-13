from rest_framework.generics import ListAPIView

from apps.base.models import City
from .serializers import CityListSerializer


class CityListAPIView(ListAPIView):
    serializer_class = CityListSerializer
    queryset = City.objects.all()


__all__ = ['CityListAPIView']
