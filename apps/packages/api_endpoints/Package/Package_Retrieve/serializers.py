from rest_framework.serializers import ModelSerializer

from apps.packages.models import Package, Plan, PlanType, PlanFeature, Activity


class PlanTypeInPlanSerializer(ModelSerializer):
    class Meta:
        model = PlanType
        fields = ['id', 'title']


class FeatureInPackageSerializer(ModelSerializer):
    class Meta:
        model = PlanFeature
        fields = ['title', 'icon', 'description']


class ActivityInPackageSerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'title', 'address', 'landmark', 'description', 'iframe', 'latitude', 'longitude']


class PlanInPackageSerializer(ModelSerializer):
    type = PlanTypeInPlanSerializer(many=False)
    features = FeatureInPackageSerializer(many=True)
    activities = ActivityInPackageSerializer(many=True)

    class Meta:
        model = Plan
        fields = ['id', 'type', 'price', 'features', 'activities', 'description']


class PackageRetrieveSerializer(ModelSerializer):
    plans = PlanInPackageSerializer(many=True)

    class Meta:
        model = Package
        fields = ['id', 'title', 'picture', 'country', 'duration', 'plans']
