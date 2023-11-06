from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.packages.models import Package


class DiscountAPITestCase(APITestCase):
    fixtures = ['test_data/fixtures/discounts']

    def setUp(self) -> None:
        Package.objects.create(title='Test package 1', description='Test description 1')
        self.url = reverse('discounts:discount_list')

    def test_discount_list_ok(self):
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
