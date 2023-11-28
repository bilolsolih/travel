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
