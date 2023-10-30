from rest_framework.generics import RetrieveAPIView

from apps.packages.models import Package
from .serializers import PackageRetrieveSerializer


class PackageRetrieveAPIView(RetrieveAPIView):
    serializer_class = PackageRetrieveSerializer
    queryset = Package.objects.filter(is_active=True)


__all__ = ['PackageRetrieveAPIView']
