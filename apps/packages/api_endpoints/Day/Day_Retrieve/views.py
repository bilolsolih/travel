from rest_framework.generics import RetrieveAPIView

from apps.packages.models import Day
from .serializers import DayRetrieveSerializer


class DayRetrieveAPIView(RetrieveAPIView):
    serializer_class = DayRetrieveSerializer

    def get_queryset(self):
        return Day.objects.filter(package_id=self.kwargs.get('package_id', None))


__all__ = ['DayRetrieveAPIView']
