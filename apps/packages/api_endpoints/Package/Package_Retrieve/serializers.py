from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.packages.models import Package, Trip, Destination, PackageFeature, Plan, PlanType, PackagePicture


class TripInPackageRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'start_date', 'get_end_date']


class DestinationInPackageRetrieveSerializer(ModelSerializer):
    ccountry = SerializerMethodField()
    ccity = SerializerMethodField()

    def get_ccountry(self, obj):
        return obj.country.title

    def get_ccity(self, obj):
        return obj.city.title

    class Meta:
        model = Destination
        fields = ['ccountry', 'ccity', 'duration']


class FeatureNestedRetrieveSerializer(ModelSerializer):
    class Meta:
        model = PackageFeature
        fields = ['id', 'title', 'icon', 'description']


class PlanTypeInPlan(ModelSerializer):
    class Meta:
        model = PlanType
        fields = ['title']
        ref_name = 'PlanTypeInPlanRetrieve'


class PlanInPackageRetrieveSerializer(ModelSerializer):
    type = PlanTypeInPlan(many=False)
    features = FeatureNestedRetrieveSerializer(many=True)

    class Meta:
        model = Plan
        fields = ['id', 'type', 'price', 'discount', 'discount_expiry_date', 'get_discounted_price', 'features', 'description']


class PictureInPackageRetrieveSerializer(ModelSerializer):
    class Meta:
        model = PackagePicture
        fields = ['id', 'picture', 'is_main']


class PackageRetrieveSerializer(ModelSerializer):
    core_features = FeatureNestedRetrieveSerializer(many=True)
    plans = PlanInPackageRetrieveSerializer(many=True)
    destinations = DestinationInPackageRetrieveSerializer(many=True)
    pictures = PictureInPackageRetrieveSerializer(many=True)
    trips = TripInPackageRetrieveSerializer(many=True)

    class Meta:
        model = Package
        fields = ['id', 'title', 'trips', 'description', 'pictures', 'get_duration', 'destinations', 'core_features', 'plans']
