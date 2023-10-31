from rest_framework import serializers

from apps.packages.models import Package


class UserLikePackageSerializer(serializers.Serializer):
    package = serializers.CharField()

    def validate(self, attrs):
        try:
            attrs['package'] = Package.objects.get(pk=attrs['package'])
        except Package.DoesNotExist:
            raise serializers.ValidationError({'package': 'No such Package in the database.'})

        return attrs
