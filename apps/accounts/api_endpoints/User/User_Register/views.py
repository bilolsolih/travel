from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserRegisterSerializer


class UserRegisterAPIView(CreateAPIView):
    parser_classes = [MultiPartParser]
    serializer_class = UserRegisterSerializer

    def generate_token(self, user):
        token = RefreshToken.for_user(user)
        return {'refresh': str(token), 'access': str(token.access_token)}

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(self.generate_token(user), status=status.HTTP_201_CREATED, headers=headers)


__all__ = ['UserRegisterAPIView']
