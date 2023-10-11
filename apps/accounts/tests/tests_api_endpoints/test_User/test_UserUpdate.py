from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from apps.accounts.models import User


class UserUpdateTestCase(APITestCase):
    def setUp(self) -> None:
        self.endpoint = reverse('accounts:update')
        defaults = {
            'first_name': 'Bilol',
            'last_name': 'Muhammad Solih',
            'phone_number': '+998912958899',
            'email': 'BilolMuhammadSolih@gmail.com',
            'password': 'Solih1234!@#$',
        }
        self.user = User.objects.create_user(**defaults)
        self.token = Token.objects.create(user=self.user)

    def test_update_ok(self):
        defaults = {
            'first_name': 'Biloliddin',
            'last_name': 'Muhammad Solih',
            'phone_number': '+998912968899',
            'email': 'BilolSolih@gmail.com',
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.patch(path=self.endpoint, data=defaults)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.filter(**defaults).first()
        self.assertIsNotNone(user)

    def test_update_not_authenticated(self):
        defaults = {
            'first_name': 'Bilolbek',
            'last_name': 'Muhammad Solih',
        }
        response = self.client.patch(path=self.endpoint, data=defaults)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
