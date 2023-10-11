from django.contrib.auth import authenticate, login, logout
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserLoginSerializer


class UserLoginAPIView(APIView):
    @swagger_auto_schema(request_body=UserLoginSerializer)
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = authenticate(username=data['login'])

        if user:
            if user.check_password(data['password']):
                login(request, user)
                return Response({'detail': 'Logged in.'}, status=status.HTTP_200_OK)
            else:
                return Response({'password': 'Wrong username/password.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'details': 'User doesn\'t exist.'}, status=status.HTTP_404_NOT_FOUND)


class UserLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response({'detail': 'Logged out.'}, status=status.HTTP_200_OK)


__all__ = ['UserLoginAPIView', 'UserLogoutAPIView']
