from rest_framework.generics import ListAPIView

from apps.packages.models import Day
from .serializers import DayListSerializer


class DayListAPIView(ListAPIView):
    serializer_class = DayListSerializer

    def get_queryset(self):
        return Day.objects.filter(package_id=self.kwargs.get('package_id', None))


__all__ = ['DayListAPIView']
