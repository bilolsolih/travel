from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from apps.accounts.models import User


class UserRetrieveTestCase(APITestCase):
    def setUp(self) -> None:
        self.endpoint = reverse('accounts:retrieve')
        defaults = {
            'first_name': 'Bilol',
            'last_name': 'Muhammad Solih',
            'phone_number': '+998912958899',
            'email': 'BilolMuhammadSolih@gmail.com',
            'password': 'Solih1234!@#$',
        }
        self.user = User.objects.create_user(**defaults)
        self.token = Token.objects.create(user=self.user)

    def test_retrieve_ok(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(path=self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('BilolMuhammadSolih@gmail.com', response.content.decode('utf-8'))

    def test_retrieve_not_authenticated(self):
        response = self.client.get(path=self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('Authentication credentials were not provided.', response.content.decode('utf-8'))
