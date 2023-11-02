from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import ModelSerializer, ValidationError

from apps.orders.models import Order, OrderStatus


class OrderCreateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['package', 'trip', 'plan']

    def create(self, validated_data):
        return self.Meta.model.objects.create(user=self.context['request'].user, price_total=validated_data['plan'].get_discounted_price, **validated_data)

    def validate(self, attrs):
        user = self.context['request'].user
        if not attrs['package'].plans.contains(attrs['plan']):
            raise ValidationError(_('No such plan in the package.'))
        if Order.objects.filter(user=user, package=attrs['package'], trip=attrs['trip'], status=OrderStatus.WAITING).exists():
            raise ValidationError(_('Order exists and waiting for payment.'))

        return attrs
