from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from apps.accounts.models import User


class UserDeleteTestCase(APITestCase):
    def setUp(self) -> None:
        self.endpoint = reverse('accounts:delete')
        defaults = {
            'first_name': 'Bilol',
            'last_name': 'Muhammad Solih',
            'phone_number': '+998912958899',
            'email': 'BilolMuhammadSolih@gmail.com',
            'password': 'Solih1234!@#$',
        }
        self.user = User.objects.create_user(**defaults)
        self.token = Token.objects.create(user=self.user)

    def test_ok(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.delete(path=self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        user = User.objects.get(phone_number='+998912958899')
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_verified)

    def test_not_authenticated(self):
        response = self.client.delete(path=self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
