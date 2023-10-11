from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserRetrieveSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserRetrieveSerializer

    def get_object(self):
        return self.request.user


__all__ = ['UserRetrieveAPIView']
