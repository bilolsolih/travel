from django.core.cache import cache
from rest_framework.generics import RetrieveAPIView

from apps.about.models import TermsAndConditions
from .serializers import TermsAndConditionsRetrieveSerializer


class TermsAndConditionsRetrieveAPIView(RetrieveAPIView):
    serializer_class = TermsAndConditionsRetrieveSerializer

    def get_object(self):
        terms = cache.get('about:terms')
        if not terms:
            terms = TermsAndConditions.objects.last()
            cache.set('about:terms', terms, timeout=60 * 60 * 6)
        return terms


__all__ = ['TermsAndConditionsRetrieveAPIView']
