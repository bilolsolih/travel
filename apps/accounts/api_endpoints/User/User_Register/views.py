from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

from .permissions import IsNotAuthenticated
from .serializers import UserRegisterSerializer


class UserRegisterAPIView(CreateAPIView):
    parser_classes = [MultiPartParser, JSONParser]
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        return serializer.save()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        token = RefreshToken.for_user(user)
        refresh_token = str(token)
        access_token = str(token.access_token)
        headers = self.get_success_headers(serializer.data)
        return Response({'refresh': refresh_token, 'access': access_token}, status=status.HTTP_201_CREATED, headers=headers)
        
        
    


__all__ = ['UserRegisterAPIView']
