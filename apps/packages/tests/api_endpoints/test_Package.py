from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .resources import *


class PackageAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        create_accommodations()  # coming from .resources
        create_packages()

    def test_package_list(self):
        response = self.client.get(reverse('packages:package_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
