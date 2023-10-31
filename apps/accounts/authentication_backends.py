from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

User = get_user_model()


class UsernamePhoneNumberAndEmailAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            return User.objects.get(phone_number=username, is_active=True)
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id, is_active=True)
        except User.DoesNotExist:
            return None
