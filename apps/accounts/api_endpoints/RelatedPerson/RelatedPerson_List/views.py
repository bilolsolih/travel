from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.accounts.models import RelatedPerson
from .serializers import RelatedPersonListSerializer


class RelatedPersonListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RelatedPersonListSerializer

    def get_queryset(self):
        return RelatedPerson.objects.filter(responsible=self.request.user)


__all__ = ['RelatedPersonListAPIView']
