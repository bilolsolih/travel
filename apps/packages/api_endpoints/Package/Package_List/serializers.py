from rest_framework.serializers import ModelSerializer

from apps.packages.models import Package, Trip, Destination, PackageFeature, Plan, PlanType


class TripInPackageListSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'start_date', 'get_end_date']


class DestinationInPackageListSerializer(ModelSerializer):
    class Meta:
        model = Destination
        fields = ['country', 'city', 'duration']


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

    class Meta:
        model = Package
        fields = ['id', 'title', 'picture', 'get_duration', 'core_features', 'plans']
