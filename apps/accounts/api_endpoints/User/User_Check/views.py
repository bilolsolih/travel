from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import User
from .serializers import UserCheckSerializer


class UserCheckAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserCheckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if User.objects.filter(phone_number=serializer.validated_data['phone_number']).exists():
            return Response({'detail': 'User exists.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'User does not exist.'}, status=status.HTTP_204_NO_CONTENT)


__all__ = ['UserCheckAPIView']
