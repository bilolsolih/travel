from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.base.models import City
from apps.packages.models import Day, Stay, Flight, Activity, ActivityBridge, Accommodation, Plan


class AccommodationInStayNestedSerializer(ModelSerializer):
    class Meta:
        model = Accommodation
        fields = ['id', 'title', 'type', 'short_description', 'rating']


class StayInDayListNestedSerializer(ModelSerializer):
    accommodation = AccommodationInStayNestedSerializer(many=False)

    class Meta:
        model = Stay
        fields = ['id', 'accommodation', 'due_time']


class CityInFlightNestedSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'title']


class FlightInDayListNestedSerializer(ModelSerializer):
    from_city = CityInFlightNestedSerializer(many=False)
    to_city = CityInFlightNestedSerializer(many=False)

    class Meta:
        model = Flight
        fields = ['id', 'from_city', 'to_city', 'due_time']


class PlanInActivityBridgeNestedSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'type']


class ActivityInActivityBridgeNestedSerializer(ModelSerializer):
    main_picture = SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', 'title', 'description', 'main_picture']

    def get_main_picture(self, instance):
        if instance.pictures.filter(is_main=True).exists():
            return instance.pictures.filter(is_main=True).first()
        else:
            return instance.pictures.first()


class ActivityBridgeInDayListSerializer(ModelSerializer):
    plan = PlanInActivityBridgeNestedSerializer(many=False)
    activity = ActivityInActivityBridgeNestedSerializer(many=False)

    class Meta:
        model = ActivityBridge
        fields = ['id', 'plan', 'activity', 'due_time']


class DayListSerializer(ModelSerializer):
    # stays = StayInDayListNestedSerializer(many=True)
    # flights = FlightInDayListNestedSerializer(many=True)
    # activities = ActivityBridgeInDayListSerializer(many=True)
    items = SerializerMethodField()

    class Meta:
        model = Day
        fields = ['id', 'day_number', 'items']
        # fields = ['id', 'day_number', 'stays', 'flights', 'activities', 'items']

    def get_items(self, instance):
        stays = StayInDayListNestedSerializer(instance.stays.all(), many=True)
        flights = FlightInDayListNestedSerializer(instance.flights.all(), many=True)
        activities = ActivityBridgeInDayListSerializer(instance.activities.all(), many=True)
        response = list(stays.data) + list(flights.data) + list(activities.data)
        return response
