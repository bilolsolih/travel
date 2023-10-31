from rest_framework.generics import RetrieveAPIView

from apps.packages.models import Day
from .serializers import DayRetrieveSerializer


class DayRetrieveAPIView(RetrieveAPIView):
    serializer_class = DayRetrieveSerializer
    queryset = Day.objects.all()
    lookup_field = 'pk'


__all__ = ['DayRetrieveAPIView']
