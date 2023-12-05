from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from apps.accounts.models import User
from .accommodations import *
from .days import *
from .packages import *


class PackageAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(phone_number='+998912958899', password='bilol2001')
        cls.token = AccessToken.for_user(cls.user)
        create_accommodations()
        create_packages()
        create_days()

    def test_package_list(self):
        response = self.client.get(reverse('packages:package_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_package_list_filter_title(self):
        url = reverse('packages:package_list') + '?title=Package%201'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Package 1')
        self.assertNotContains(response, 'Package 2')

    def test_package_list_filter_popular_places(self):
        url = reverse('packages:package_list') + '?popular_places=1'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Package 1')
        self.assertNotContains(response, 'Package 2')

        url = reverse('packages:package_list') + '?popular_places=3'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Package 2')
        self.assertNotContains(response, 'Package 1')

    def test_package_list_filter_date(self):
        url = reverse('packages:package_list') + '?start_date=2024-01-01&end_date=2024-02-01'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Package 1')
        self.assertNotContains(response, 'Package 2')

        url = reverse('packages:package_list') + '?start_date=2024-02-01&end_date=2024-02-06'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Package 2')
        self.assertNotContains(response, 'Package 1')

        url = reverse('packages:package_list') + '?start_date=2023-01-01&end_date=2023-02-01'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotContains(response, 'Package 1')
        self.assertNotContains(response, 'Package 2')

    def test_package_list_filter_country(self):
        url = reverse('packages:package_list') + '?country=1'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Package 1')
        self.assertNotContains(response, 'Package 2')
        self.assertNotContains(response, 'Package 3')

        url = reverse('packages:package_list') + '?country=2'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Package 2')
        self.assertNotContains(response, 'Package 1')
        self.assertNotContains(response, 'Package 3')

        url = reverse('packages:package_list') + '?country=3'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Package 3')
        self.assertNotContains(response, 'Package 1')
        self.assertNotContains(response, 'Package 2')

    def test_package_list_filter_city(self):
        url = reverse('packages:package_list') + '?city=1'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Package 1')
        self.assertContains(response, 'Package 3')
        self.assertNotContains(response, 'Package 2')

        url = reverse('packages:package_list') + '?city=4'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Package 2')
        self.assertNotContains(response, 'Package 1')
        self.assertNotContains(response, 'Package 3')

    def test_package_list_pagination(self):
        url = reverse('packages:package_list') + '?limit=1&offset=0'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Package 1')
        self.assertNotContains(response, 'Package 2')
        self.assertNotContains(response, 'Package 3')

        url = reverse('packages:package_list') + '?limit=2&offset=0'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Package 1')
        self.assertContains(response, 'Package 2')
        self.assertNotContains(response, 'Package 3')

        url = reverse('packages:package_list') + '?limit=1&offset=2'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Package 3')
        self.assertNotContains(response, 'Package 1')
        self.assertNotContains(response, 'Package 2')

    def test_package_retrieve(self):
        urls = [reverse('packages:package_retrieve', args=[package_id]) for package_id in range(1, 4)]
        for url in urls:
            response = self.client.get(path=url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_package_liked_auth(self):
        self.user.liked_packages.add(2, 3)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.get(path=reverse('packages:package_liked_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Package 2')
        self.assertContains(response, 'Package 3')

    def test_package_liked_auth_empty(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.get(path=reverse('packages:package_liked_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, b'[]')

    def test_package_liked_non_auth(self):
        response = self.client.get(path=reverse('packages:package_liked_list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_day_retrieve(self):
        urls = [reverse('packages:day_retrieve', args=[day_id]) for day_id in range(1, 10)]
        for url in urls:
            response = self.client.get(path=url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertContains(response, 'day_number')

    def test_accommodation_list(self):
        response = self.client.get(path=reverse('packages:accommodation_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Title 1')

    def test_accommodation_retrieve(self):
        urls = [reverse('packages:accommodation_retrieve', args=[accommodation_id]) for accommodation_id in range(1, 4)]
        for url in urls:
            response = self.client.get(path=url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertContains(response, 'title')

    def test_activity_retrieve(self):
        urls = [reverse('packages:activity_retrieve', args=[activity_id]) for activity_id in range(1, 4)]
        for url in urls:
            response = self.client.get(path=url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertContains(response, 'title')

