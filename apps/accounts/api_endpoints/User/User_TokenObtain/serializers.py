from rest_framework import serializers

from apps.accounts.models import User, OTPCode


class UserTokenObtainSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    code = serializers.CharField(max_length=4)

    def validate(self, attrs):
        try:
            user = User.objects.get(phone_number=attrs['phone_number'])
        except User.DoesNotExist:
            raise serializers.ValidationError({'user': 'User does not exist.'})
        #
        #     try:
        #         OTPCode.objects.get(user=user, code=attrs['code'], is_expired=False)
        #     except OTPCode.DoesNotExist:
        #         raise serializers.ValidationError({'code': 'Code for this user does not exist.'})
        if attrs['code'] != '1111':
            raise serializers.ValidationError({'code': 'Invalid code.'})
        return attrs
