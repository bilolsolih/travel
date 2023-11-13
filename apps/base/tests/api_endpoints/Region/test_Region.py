from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class RegionAPITestCase(APITestCase):
    fixtures = ['test_data/fixtures/base_region']

    def setUp(self) -> None:
        self.url = reverse('base:region_list')

    def test_region_list(self):
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
