from datetime import timedelta

from django.db.models import Sum
from django.utils import timezone
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.packages.models import Package, Trip, Destination, PackageFeature, Plan, PlanType


class TripInPackageListSerializer(ModelSerializer):
    end_date = SerializerMethodField()

    class Meta:
        model = Trip
        fields = ['id', 'start_date', 'end_date']

    def get_end_date(self, instance):
        if instance.package.destinations.exists():
            duration = instance.package.destinations.aggregate(total_duration=Sum('duration'))['total_duration']
            return instance.start_date + timedelta(days=duration)
        else:
            return None


class DestinationInPackageListSerializer(ModelSerializer):
    ccity = SerializerMethodField()

    def get_ccity(self, instance):
        return instance.city.title

    class Meta:
        model = Destination
        fields = ['ccity', 'duration']


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
    type = SerializerMethodField()
    features = FeatureNestedListSerializer(many=True)
    discounted_price = SerializerMethodField()

    class Meta:
        model = Plan
        fields = ['id', 'type', 'price', 'discount', 'discount_expiry_date', 'discounted_price', 'features']

    def get_discounted_price(self, instance):
        if instance.discount and instance.discount_expiry_date and instance.discount_expiry_date > timezone.now():
            return instance.price * ((100 - instance.discount) / 100)
        else:
            return instance.price

    def get_type(self, instance):
        return instance.type.title


class PackageListSerializer(ModelSerializer):
    core_features = FeatureNestedListSerializer(many=True)
    plans = PlanInPackageListSerializer(many=True)
    destinations = DestinationInPackageListSerializer(many=True)
    trips = TripInPackageListSerializer(many=True)
    is_liked = SerializerMethodField()
    picture = SerializerMethodField()
    duration = SerializerMethodField()

    class Meta:
        model = Package
        fields = ['id', 'title', 'trips', 'picture', 'duration', 'country', 'destinations', 'core_features', 'plans', 'is_liked']

    def get_duration(self, instance):
        if instance.destinations.exists():
            return instance.destinations.aggregate(total_duration=Sum('duration'))['total_duration']
        else:
            return None

    def get_picture(self, instance):
        pictures = instance.pictures.all()
        if pictures.exists():
            if pictures.filter(is_main=True).exists():
                url = pictures.filter(is_main=True).first().picture.url
            else:
                url = pictures.first().picture.url
            return self.context['request'].build_absolute_uri(url)
        else:
            return None

    def get_is_liked(self, instance):
        user = self.context['request'].user
        if user.is_authenticated and user.liked_packages.contains(instance):
            return True
        else:
            return False
