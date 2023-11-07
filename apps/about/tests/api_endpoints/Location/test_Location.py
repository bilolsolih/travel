from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class LocationAPITestCase(APITestCase):
    fixtures = ['test_data/fixtures/about', 'test_data/fixtures/base']

    @classmethod
    def setUpTestData(cls):
        cls.urls = {
            'list': reverse('about:location_list'),
            'retrieve_1': reverse('about:location_retrieve', kwargs={'pk': 1}),
            'retrieve_2': reverse('about:location_retrieve', kwargs={'pk': 2}),
        }

    def test_location_list(self):
        response = self.client.get(path=self.urls['list'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_location_retrieve(self):
        response_1 = self.client.get(path=self.urls['retrieve_1'])
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)

        response_2 = self.client.get(path=self.urls['retrieve_2'])
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)
