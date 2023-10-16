from rest_framework.generics import ListAPIView

from apps.base.models import Region
from .serializers import RegionListSerializer


class RegionListAPIView(ListAPIView):
    serializer_class = RegionListSerializer
    queryset = Region.objects.all()


__all__ = ['RegionListAPIView']
