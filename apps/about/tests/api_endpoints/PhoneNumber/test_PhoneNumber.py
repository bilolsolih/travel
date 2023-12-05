from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .phone_numbers import *


class PhoneNumberAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('about:phone_number_retrieve')
        create_phone_number()

    def test_phone_number_retrieve(self):
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, '+998902958899')
        self.assertNotContains(response, '+998912958899')
