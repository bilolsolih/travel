from datetime import timedelta

from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.packages.models import Package, Trip, Destination, PackageFeature, Plan, PlanType, PackagePicture, Day


class TripInPackageRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'start_date', 'get_end_date']


class DestinationInPackageRetrieveSerializer(ModelSerializer):
    ccity = SerializerMethodField()

    def get_ccity(self, obj):
        return obj.city.title

    class Meta:
        model = Destination
        fields = ['ccity', 'duration']


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


class DayInPackageRetrieveSerializer(ModelSerializer):
    date = SerializerMethodField()

    class Meta:
        model = Day
        fields = ['id', 'day_number', 'date']

    def get_date(self, instance):
        if instance.package.trips.exists():
            return instance.package.trips.last().start_date + timedelta(days=(instance.day_number - 1))
        else:
            return None


class PackageRetrieveSerializer(ModelSerializer):
    core_features = FeatureNestedRetrieveSerializer(many=True)
    plans = PlanInPackageRetrieveSerializer(many=True)
    destinations = DestinationInPackageRetrieveSerializer(many=True)
    pictures = PictureInPackageRetrieveSerializer(many=True)
    trips = TripInPackageRetrieveSerializer(many=True)
    days = DayInPackageRetrieveSerializer(many=True)

    class Meta:
        model = Package
        fields = ['id', 'title', 'trips', 'description', 'country', 'pictures', 'get_duration', 'destinations', 'core_features', 'plans', 'days']
