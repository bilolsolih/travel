from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import User, OTPCode
from .serializers import UserCheckSerializer
from random import randint


class UserCheckAPIView(APIView):
    def generate_otp(self, user):
        if OTPCode.objects.filter(user=user).exists():
            OTPCode.objects.filter(user=user).delete()
        return OTPCode.objects.create(user=user, code=randint(1000, 9999))

    def post(self, request, *args, **kwargs):
        serializer = UserCheckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = User.objects.get(**serializer.validated_data)
            self.generate_otp(user)
            return Response({'detail': 'User exists.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'detail': 'User does not exist.'}, status=status.HTTP_204_NO_CONTENT)


__all__ = ['UserCheckAPIView']
