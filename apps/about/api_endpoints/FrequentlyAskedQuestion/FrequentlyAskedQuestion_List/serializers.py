from rest_framework.serializers import ModelSerializer

from apps.about.models import FrequentlyAskedQuestion


class FrequentlyAskedQuestionListSerializer(ModelSerializer):
    class Meta:
        model = FrequentlyAskedQuestion
        fields = ['id', 'question', 'answer']
