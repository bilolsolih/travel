from rest_framework.generics import ListAPIView

from apps.about.models import SocialMedia
from .serializers import SocialMediaListSerializer


class SocialMediaListAPIView(ListAPIView):
    serializer_class = SocialMediaListSerializer
    queryset = SocialMedia.objects.all()


__all__ = ['SocialMediaListAPIView']
