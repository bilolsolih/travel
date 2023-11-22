from rest_framework.serializers import ModelSerializer
from apps.payments.models import Payment, Category


class CategoryInPaymentList(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class PaymentListSerializer(ModelSerializer):
    category = CategoryInPaymentList(many=False)

    class Meta:
        model = Payment
        fields = ['id', 'category', 'payee', 'responsible', 'amount', 'status', 'created']
