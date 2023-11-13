from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CityAPITestCase(APITestCase):
    fixtures = ['test_data/fixtures/base_city_and_country']

    def setUp(self) -> None:
        self.url = reverse('base:city_list')

    def test_city_list(self):
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
