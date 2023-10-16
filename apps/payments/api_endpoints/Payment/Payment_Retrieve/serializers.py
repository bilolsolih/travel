from rest_framework.serializers import ModelSerializer

from apps.payments.models import Payment, Category


class CategoryInPayment(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class PaymentRetrieveSerializer(ModelSerializer):
    category = CategoryInPayment(many=False)

    class Meta:
        model = Payment
        fields = ['id', 'category', 'payer', 'payee', 'responsible', 'description', 'amount']
