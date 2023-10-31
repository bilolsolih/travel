from rest_framework.serializers import ModelSerializer
from apps.packages.models import Day


class DayListSerializer(ModelSerializer):
    class Meta:
        model = Day
        fields = ['id', 'day_number']
