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
        }

    def test_ok(self):
        response = self.client.post(path=self.endpoint, data=self.defaults)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(phone_number=self.defaults['phone_number']).exists())