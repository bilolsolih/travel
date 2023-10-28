from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import User, OTPCode
from .serializers import UserCheckSerializer
from random import randint


class UserCheckAPIView(APIView):
    def generate_otp(self, phone_number):
        if OTPCode.objects.filter(phone_number=phone_number).exists():
            OTPCode.objects.filter(phone_number=phone_number).delete()
        return OTPCode.objects.create(phone_number=phone_number, code=randint(1000, 9999))

    def post(self, request, *args, **kwargs):
        serializer = UserCheckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = User.objects.get(**serializer.validated_data)
            exist = True
        except User.DoesNotExist:
            exist = False
        self.generate_otp(serializer.validated_data["phone_number"])
        return Response({'exist': exist}, status=status.HTTP_200_OK)


__all__ = ['UserCheckAPIView']
