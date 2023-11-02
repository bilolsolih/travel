from rest_framework.serializers import ModelSerializer

from apps.discounts.models import Discount


class DiscountListSerializer(ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'title', 'description', 'max_discount', 'expiry_date']
