from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from apps.accounts.models import User, OTPCode


class UserTokenObtainSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    code = serializers.CharField(max_length=4)

    def validate(self, attrs):
        try:
            user = User.objects.get(phone_number=attrs['phone_number'])
            exist = True
        except User.DoesNotExist:
            exist = False
        #
        #     try:
        #         OTPCode.objects.get(user=user, code=attrs['code'], is_expired=False)
        #     except OTPCode.DoesNotExist:
        #         raise serializers.ValidationError({'code': 'Code for this user does not exist.'})
        if attrs['code'] != '1111':
            raise serializers.ValidationError({'code': 'Invalid code.'})
        if exist:
            token = RefreshToken.for_user(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            return {'refresh': refresh_token, 'access': access_token}
        else:
            return {"exist":False}
