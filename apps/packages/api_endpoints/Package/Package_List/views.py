from rest_framework.generics import ListAPIView

from apps.packages.models import Package
from .serializers import PackageListSerializer


class PackageListAPIView(ListAPIView):
    serializer_class = PackageListSerializer
    queryset = Package.objects.filter(is_active=True)


__all__ = ['PackageListAPIView']
