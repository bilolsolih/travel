from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserTokenObtainSerializer


class UserTokenObtainAPIView(TokenObtainPairView):
    serializer_class = UserTokenObtainSerializer


__all__ = ['UserTokenObtainAPIView']
