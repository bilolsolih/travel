from rest_framework.serializers import ModelSerializer

from apps.about.models import SocialMedia


class SocialMediaListSerializer(ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['id', 'icon', 'link']
