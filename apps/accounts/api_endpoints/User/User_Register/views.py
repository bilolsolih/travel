from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser

from .permissions import IsNotAuthenticated
from .serializers import UserRegisterSerializer


class UserRegisterAPIView(CreateAPIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsNotAuthenticated]
    serializer_class = UserRegisterSerializer


__all__ = ['UserRegisterAPIView']
