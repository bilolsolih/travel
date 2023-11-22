from rest_framework.serializers import ModelSerializer

from apps.payments.models import Payment, Category


class CategoryInPaymentRetrieve(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class PaymentRetrieveSerializer(ModelSerializer):
    category = CategoryInPaymentRetrieve(many=False)

    class Meta:
        model = Payment
        fields = ['id', 'category', 'payer', 'payee', 'responsible', 'description', 'amount']
