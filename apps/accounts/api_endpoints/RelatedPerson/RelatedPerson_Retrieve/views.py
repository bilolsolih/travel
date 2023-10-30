from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.accounts.models import RelatedPerson
from .serializers import RelatedPersonRetrieveSerializer


class RelatedPersonRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RelatedPersonRetrieveSerializer

    def get_queryset(self):
        queryset = RelatedPerson.objects.filter(responsible=self.request.user)
        return queryset


__all__ = ['RelatedPersonRetrieveAPIView']
