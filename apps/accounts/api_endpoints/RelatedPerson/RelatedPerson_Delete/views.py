from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.accounts.models import RelatedPerson


class RelatedPersonDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return RelatedPerson.objects.filter(responsible=self.request.user)


__all__ = ['RelatedPersonDeleteAPIView']
