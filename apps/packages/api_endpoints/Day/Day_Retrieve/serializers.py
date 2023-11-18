from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.base.models import City
from apps.packages.models import Day, Stay, Flight, Activity, ActivityBridge, Accommodation, Plan, AccommodationType


class TypeInAccommodationInStay(ModelSerializer):
    class Meta:
        model = AccommodationType
        fields = ['id', 'title']


class AccommodationInStayNestedSerializer(ModelSerializer):
    type = TypeInAccommodationInStay(many=False)
    picture = SerializerMethodField()

    class Meta:
        model = Accommodation
        fields = ['id', 'title', 'type', 'short_description', 'rating', 'picture']

    def get_picture(self, instance):
        request = self.context['request']
        pictures = instance.pictures.all()
        if pictures.exists():
            if pictures.filter(is_main=True).exists:
                url = pictures.filter(is_main=True).first().picture.url
            else:
                url = pictures.first().picture.url
            return request.build_absolute_uri(url)
        else:
            return None


class StayInDayRetrieveNestedSerializer(ModelSerializer):
    accommodation = AccommodationInStayNestedSerializer(many=False)
    type = SerializerMethodField()

    class Meta:
        model = Stay
        fields = ['id', 'type', 'accommodation', 'due_time']

    def get_type(self, instance):
        return 'stay'


class CityInFlightNestedSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'title']


class FlightInDayRetrieveNestedSerializer(ModelSerializer):
    from_city = CityInFlightNestedSerializer(many=False)
    to_city = CityInFlightNestedSerializer(many=False)
    type = SerializerMethodField()

    class Meta:
        model = Flight
        fields = ['id', 'type', 'from_city', 'to_city', 'due_time']

    def get_type(self, instance):
        return 'flight'


class PlanInActivityBridgeNestedSerializer(ModelSerializer):
    plan_type = SerializerMethodField()

    class Meta:
        model = Plan
        fields = ['id', 'plan_type']

    def get_plan_type(self, instance):
        return instance.type.title


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
    type = SerializerMethodField()

    class Meta:
        model = ActivityBridge
        fields = ['id', 'type', 'plan', 'activity', 'due_time']

    def get_type(self, instance):
        return 'activity'


class DayRetrieveSerializer(ModelSerializer):
    items = SerializerMethodField()

    class Meta:
        model = Day
        fields = ['id', 'day_number', 'items']

    def get_items(self, instance):
        stays = StayInDayRetrieveNestedSerializer(instance.stays.all(), many=True)
        flights = FlightInDayRetrieveNestedSerializer(instance.flights.all(), many=True)
        activities = ActivityBridgeInDayRetrieveSerializer(instance.activities.all(), many=True)
        response = list(stays.data) + list(flights.data) + list(activities.data)
        response.sort(key=lambda x: x['due_time'])
        return response
