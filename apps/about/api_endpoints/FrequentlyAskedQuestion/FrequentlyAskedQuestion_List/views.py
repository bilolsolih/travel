from django.core.cache import cache
from rest_framework.generics import ListAPIView

from apps.about.models import FrequentlyAskedQuestion
from .serializers import FrequentlyAskedQuestionListSerializer


class FrequentlyAskedQuestionListAPIView(ListAPIView):
    serializer_class = FrequentlyAskedQuestionListSerializer

    def get_queryset(self):
        queryset = cache.get('about:questions')
        if not queryset:
            queryset = FrequentlyAskedQuestion.objects.all()
            cache.set('about:questions', queryset, timeout=60 * 60 * 6)
        return queryset


__all__ = ['FrequentlyAskedQuestionListAPIView']
