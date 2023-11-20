from rest_framework.serializers import ModelSerializer

from apps.packages.models import Activity, ActivityPicture


class ActivityPictureInActivityRetrieveSerializer(ModelSerializer):
    class Meta:
        model = ActivityPicture
        fields = ['id', 'picture', 'is_main']


class ActivityRetrieveSerializer(ModelSerializer):
    pictures = ActivityPictureInActivityRetrieveSerializer(many=True)

    class Meta:
        model = Activity
        fields = ['id', 'title', 'address', 'landmark', 'description', 'iframe', 'latitude', 'longitude', 'pictures']
