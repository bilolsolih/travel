from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.orders.models import Order
from apps.packages.models import Package, Plan


class PackageInOrderSerializer(ModelSerializer):
    picture = SerializerMethodField()

    class Meta:
        model = Package
        fields = ['id', 'title', 'picture']

    def get_picture(self, instance):
        pictures = instance.pictures.all()
        if pictures.exists():
            if pictures.filter(is_main=True).exists():
                url = pictures.get(is_main=True).picture.url
            else:
                url = pictures.last().picture.url
            return self.context['request'].build_absolute_uri(url)
        else:
            return None


class PlanInOrder(ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'type']
        depth = 1


class OrderListSerializer(ModelSerializer):
    package = SerializerMethodField()
    plan = PlanInOrder(many=False)

    class Meta:
        model = Order
        fields = ['package', 'plan', 'price_total', 'price_paid', 'get_price_to_pay', 'status']

    def get_package(self, instance):
        package = PackageInOrderSerializer(instance.package, many=False, context={'request': self.context['request']})
        return package.data
