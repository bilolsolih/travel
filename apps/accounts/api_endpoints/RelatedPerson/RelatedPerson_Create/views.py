from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import RelatedPersonCreateSerializer


class RelatedPersonCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RelatedPersonCreateSerializer

    def perform_create(self, serializer):
        serializer.save(responsible=self.request.user)


__all__ = ['RelatedPersonCreateAPIView']
