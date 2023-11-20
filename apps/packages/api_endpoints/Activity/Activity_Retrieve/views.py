from rest_framework.generics import RetrieveAPIView

from apps.packages.models import Activity
from .serializers import ActivityRetrieveSerializer


class ActivityRetrieveAPIView(RetrieveAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivityRetrieveSerializer


__all__ = ['ActivityRetrieveAPIView']
