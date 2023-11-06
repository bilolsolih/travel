import json
from datetime import timedelta

from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from apps.accounts.models import User, OTPCode, VerifiedPhoneNumber


class UserAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.urls = {
            'check': reverse('accounts:check'),
            'token_obtain': reverse('accounts:token_obtain'),
            'register': reverse('accounts:register'),
            'login': reverse('accounts:login'),
            'logout': reverse('accounts:logout'),
            'delete': reverse('accounts:delete'),
            'retrieve': reverse('accounts:retrieve'),
            'update': reverse('accounts:update'),
        }
        cls.data = {
            'first_name': 'Bilol',
            'last_name': 'Muhammad Solih',
            'phone_number': '+998901234567',
        }
        cls.phone_number = '+998912345678'
        User.objects.create(**cls.data)

    def get_content(self, response):
        return json.loads(response.content.decode('utf-8'))

    # NOT REGISTERED SCENARIOS #
    def test_check_phone_number_not_registered(self):
        response = self.client.post(path=self.urls['check'], data={'phone_number': self.phone_number})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(self.get_content(response)['exist'])
        otps = OTPCode.objects.filter(phone_number=self.phone_number)
        self.assertEqual(otps.count(), 1)
        self.assertLess(timezone.now() - otps.first().created, timedelta(seconds=5))

    def test_token_obtain_not_registered(self):
        response = self.client.post(path=self.urls['token_obtain'], data={'phone_number': self.phone_number, 'code': '1111'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(VerifiedPhoneNumber.objects.filter(phone_number=self.phone_number).exists())
        self.assertFalse(self.get_content(response)['exist'])

    # REGISTERED SCENARIOS #
    def test_check_phone_number_registered(self):
        response = self.client.post(path=self.urls['check'], data={'phone_number': self.data['phone_number']})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.get_content(response)['exist'])
        otps = OTPCode.objects.filter(phone_number=self.data['phone_number'])
        self.assertEqual(otps.count(), 1)
        self.assertLess(timezone.now() - otps.first().created, timedelta(seconds=2))

    def test_token_obtain_registered(self):
        response = self.client.post(path=self.urls['token_obtain'], data={'phone_number': self.data['phone_number'], 'code': '1111'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.get_content(response)['exist'])
        self.assertContains(response, 'refresh')
        self.assertContains(response, 'access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_content(response)["access"]}')
        mock_response = self.client.get(path=self.urls['retrieve'])
        self.assertEqual(mock_response.status_code, status.HTTP_200_OK)
        self.assertContains(mock_response, self.data['phone_number'])
