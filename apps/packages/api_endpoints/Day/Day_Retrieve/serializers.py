from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.base.models import City
from apps.packages.models import Day, Stay, Flight, Activity, ActivityBridge, Accommodation, Plan


class AccommodationInStayNestedSerializer(ModelSerializer):
    class Meta:
        model = Accommodation
        fields = ['id', 'title', 'type', 'short_description', 'rating']


class StayInDayRetrieveNestedSerializer(ModelSerializer):
    accommodation = AccommodationInStayNestedSerializer(many=False)

    class Meta:
        model = Stay
        fields = ['id', 'accommodation', 'due_time']


class CityInFlightNestedSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'title']


class FlightInDayRetrieveNestedSerializer(ModelSerializer):
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


class ActivityBridgeInDayRetrieveSerializer(ModelSerializer):
    plan = PlanInActivityBridgeNestedSerializer(many=False)
    activity = ActivityInActivityBridgeNestedSerializer(many=False)

    class Meta:
        model = ActivityBridge
        fields = ['id', 'plan', 'activity', 'due_time']


class DayRetrieveSerializer(ModelSerializer):
    stays = StayInDayRetrieveNestedSerializer(many=True)
    flights = FlightInDayRetrieveNestedSerializer(many=True)
    activities = ActivityBridgeInDayRetrieveSerializer(many=True)

    class Meta:
        model = Day
        fields = ['id', 'day_number', 'stays', 'flights', 'activities']
