from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class PopularPlaceAPITestCase(APITestCase):
    fixtures = ['test_data/fixtures/popular_places']

    def setUp(self) -> None:
        self.list_url = reverse('places:popular_place_list')
        self.retrieve_url_1 = reverse('places:popular_place_retrieve', kwargs={'pk': '1'})
        self.retrieve_url_2 = reverse('places:popular_place_retrieve', kwargs={'pk': '2'})

    def test_popular_place_list(self):
        response = self.client.get(path=self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Popular place 1')
        self.assertContains(response, 'Popular place 2')

    def test_popular_place_retrieve(self):
        response_1 = self.client.get(path=self.retrieve_url_1)
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertContains(response_1, 'Popular place 1')

        response_2 = self.client.get(path=self.retrieve_url_2)
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)
        self.assertContains(response_2, 'Popular place 2')
