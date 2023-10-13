from rest_framework.serializers import ModelSerializer

from apps.orders.models import Order
from apps.packages.models import Package, Plan


class PackageInOrderSerializer(ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'title']


class PlanInOrder(ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'type']
        depth = 1


class OrderListSerializer(ModelSerializer):
    package = PackageInOrderSerializer(many=False)
    plan = PlanInOrder(many=False)

    class Meta:
        model = Order
        fields = ['package', 'plan', 'price_total', 'price_paid', 'get_price_to_pay', 'status']
