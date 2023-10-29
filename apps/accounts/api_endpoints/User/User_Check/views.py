from random import randint

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import User, OTPCode
from .serializers import UserCheckSerializer


class UserCheckAPIView(APIView):
    def generate_otp(self, validated_data):
        if OTPCode.objects.filter(**validated_data).exists():
            OTPCode.objects.filter(**validated_data).delete()
        return OTPCode.objects.create(code=randint(1000, 9999), **validated_data)

    @swagger_auto_schema(request_body=UserCheckSerializer)
    def post(self, request, *args, **kwargs):
        serializer = UserCheckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            User.objects.get(**serializer.validated_data)
            exist = True
        except User.DoesNotExist:
            exist = False
        self.generate_otp(serializer.validated_data)

        return Response({'exist': exist}, status=status.HTTP_200_OK)


__all__ = ['UserCheckAPIView']
