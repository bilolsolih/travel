from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserTokenObtainSerializer


class UserTokenObtainAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserTokenObtainSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


__all__ = ['UserTokenObtainAPIView']
