from django.contrib.auth import logout
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated


class UserDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.is_verified = False
        instance.save()
        logout(self.request)

    def get_object(self):
        return self.request.user


__all__ = ['UserDeleteAPIView']
