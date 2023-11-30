from datetime import timedelta

from django.utils import timezone
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.packages.models import Package, Trip, Destination, PackageFeature, Plan, PlanType, PackagePicture, Day


class TripInPackageRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'start_date', 'end_date']


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
    discounted_price = SerializerMethodField()

    class Meta:
        model = Plan
        fields = ['id', 'type', 'price', 'is_discount_active', 'discount', 'discount_expiry_date', 'discounted_price', 'features', 'description']

    def get_discounted_price(self, instance):
        if instance.is_discount_active and instance.discount and instance.discount_expiry_date and instance.discount_expiry_date > timezone.now():
            return instance.price * ((100 - instance.discount) / 100)
        else:
            return instance.price


class PictureInPackageRetrieveSerializer(ModelSerializer):
    class Meta:
        model = PackagePicture
        fields = ['id', 'picture', 'is_main']


class DayInPackageRetrieveSerializer(ModelSerializer):

    class Meta:
        model = Day
        fields = ['id', 'day_number', 'date']


class PackageRetrieveSerializer(ModelSerializer):
    core_features = FeatureNestedRetrieveSerializer(many=True)
    plans = PlanInPackageRetrieveSerializer(many=True)
    destinations = DestinationInPackageRetrieveSerializer(many=True)
    pictures = PictureInPackageRetrieveSerializer(many=True)
    trips = TripInPackageRetrieveSerializer(many=True)
    days = DayInPackageRetrieveSerializer(many=True)

    class Meta:
        model = Package
        fields = ['id', 'title', 'trips', 'description', 'country', 'pictures', 'duration', 'destinations', 'core_features', 'plans', 'days']
