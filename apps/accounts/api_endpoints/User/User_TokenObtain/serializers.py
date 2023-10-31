from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from apps.accounts.models import User, VerifiedPhoneNumber


class UserTokenObtainSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    code = serializers.CharField(max_length=4, min_length=4)

    def validate(self, attrs):
        # try:
        #     OTPCode.objects.get(phone_number=attrs['phone_number'], code=attrs['code'], is_expired=False)
        # except OTPCode.DoesNotExist:
        #     raise serializers.ValidationError({'code': 'Either Phone number or Code is wrong.'})
        user = User.objects.filter(phone_number=attrs['phone_number']).first()
        if user:
            token = RefreshToken.for_user(user)
            return {'refresh': str(token), 'access': str(token.access_token), 'exist': True}
        else:
            VerifiedPhoneNumber.objects.create(phone_number=attrs['phone_number'])
            return {'exist': False}
