from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .resources import *


class DiscountAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        create_discounts_and_packages()
        cls.url = reverse('discounts:discount_list')

    def test_discount_list_ok(self):
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
