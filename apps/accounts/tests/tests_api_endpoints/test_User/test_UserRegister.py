from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.accounts.models import User


class UserRegisterTestCase(APITestCase):
    def setUp(self) -> None:
        self.endpoint = reverse('accounts:register')
        self.defaults = {
            'first_name': 'Bilol',
            'last_name': 'Muhammad Solih',
            'phone_number': '+998912958899',
            'email': 'BilolMuhammadSolih@gmail.com',
            'password': 'Solih1234!@#$',
            'password_check': 'Solih1234!@#$'
        }

    def test_ok(self):
        response = self.client.post(path=self.endpoint, data=self.defaults)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(phone_number=self.defaults['phone_number']).exists())

    def test_unmatching_passwords(self):
        self.defaults['password_check'] = 'Solih1234'
        response = self.client.post(path=self.endpoint, data=self.defaults)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Passwords do not match.', response.content.decode('utf-8'))
