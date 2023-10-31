from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.packages.models import Package, Trip, Destination, PackageFeature, Plan, PlanType


class TripInPackageListSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'start_date', 'get_end_date']


class DestinationInPackageListSerializer(ModelSerializer):
    ccountry = SerializerMethodField()
    ccity = SerializerMethodField()

    def get_ccountry(self, obj):
        return obj.country.title

    def get_ccity(self, obj):
        return obj.city.title

    class Meta:
        model = Destination
        fields = ['ccountry', 'ccity', 'duration']


class FeatureNestedListSerializer(ModelSerializer):
    class Meta:
        model = PackageFeature
        fields = ['id', 'title', 'icon']


class PlanTypeInPlan(ModelSerializer):
    class Meta:
        model = PlanType
        fields = ['title']
        ref_name = 'PlanTypeInPlanList'


class PlanInPackageListSerializer(ModelSerializer):
    type = PlanTypeInPlan(many=False)
    features = FeatureNestedListSerializer(many=True)

    class Meta:
        model = Plan
        fields = ['id', 'type', 'price', 'discount', 'discount_expiry_date', 'get_discounted_price', 'features']


class PackageListSerializer(ModelSerializer):
    core_features = FeatureNestedListSerializer(many=True)
    plans = PlanInPackageListSerializer(many=True)
    destinations = DestinationInPackageListSerializer(many=True)
    trips = TripInPackageListSerializer(many=True)
    is_liked = SerializerMethodField()

    class Meta:
        model = Package
        fields = ['id', 'title', 'trips', 'picture', 'get_duration', 'get_discount', 'destinations', 'core_features', 'plans', 'is_liked']

    def get_is_liked(self, instance):
        user = self.context['request'].user
        if user.is_authenticated and user.liked_packages.contains(instance):
            return True
        else:
            return False
