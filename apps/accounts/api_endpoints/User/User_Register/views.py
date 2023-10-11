from rest_framework.generics import CreateAPIView

from .permissions import IsNotAuthenticated
from .serializers import UserRegisterSerializer


class UserRegisterAPIView(CreateAPIView):
    permission_classes = [IsNotAuthenticated]
    serializer_class = UserRegisterSerializer


__all__ = ['UserRegisterAPIView']
