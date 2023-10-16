from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import ModelSerializer, ValidationError

from apps.orders.models import Order, OrderStatus
from apps.packages.models import Package, Plan


class OrderCreateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['package', 'plan']

    def create(self, validated_data):
        return self.Meta.model.objects.create(user=self.context['request'].user, price_total=validated_data['plan'].get_discounted_price, **validated_data)

    def validate(self, attrs):
        user = self.context['request'].user

        if attrs['plan'] not in attrs['package'].plans.all():
            raise ValidationError(_('No such plan in the package.'))

        if Order.objects.filter(user=user, package=attrs['package'], status=OrderStatus.WAITING).exists():
            raise ValidationError(_('Order exists and waiting for payment.'))
        
        return attrs
