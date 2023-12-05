from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .popular_places import *


class PopularPlaceAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.list_url = reverse('places:popular_place_list')
        create_places()

    def test_popular_place_list(self):
        response = self.client.get(path=self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Popular place 1')
        self.assertContains(response, 'Popular place 2')
