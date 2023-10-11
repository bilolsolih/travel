from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from apps.accounts.models import User


class UserLoginLogoutTestCase(APITestCase):
    def setUp(self) -> None:
        self.login_endpoint = reverse('accounts:login')
        self.logout_endpoint = reverse('accounts:logout')
        defaults = {
            'first_name': 'Bilol',
            'last_name': 'Muhammad Solih',
            'phone_number': '+998912958899',
            'email': 'BilolMuhammadSolih@gmail.com',
            'password': 'Solih1234!@#$',
        }
        self.user = User.objects.create_user(**defaults)
        self.token = Token.objects.create(user=self.user)

    def test_login_ok_with_phone_number(self):
        response = self.client.post(path=self.login_endpoint, data={
            'login': '+998912958899',
            'password': 'Solih1234!@#$'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_ok_with_email(self):
        response = self.client.post(path=self.login_endpoint, data={
            'login': 'BilolMuhammadSolih@gmail.com',
            'password': 'Solih1234!@#$'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_wrong_password(self):
        response = self.client.post(path=self.login_endpoint, data={
            'login': '+998912958899',
            'password': 'SomeWrongPassword'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Wrong username/password.', response.content.decode('utf-8'))

    def test_login_disabled_user(self):
        self.user.is_active = False
        self.user.save(update_fields=['is_active'])
        response = self.client.post(path=self.login_endpoint, data={
            'login': '+998912958899',
            'password': 'Solih1234!@#$'
        })
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('User doesn\'t exist.', response.content.decode('utf-8'))

    def test_logout_ok(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(path=self.logout_endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Logged out.', response.content.decode('utf-8'))

    def test_logout_not_authenticated(self):
        response = self.client.get(path=self.logout_endpoint)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('Authentication credentials were not provided.', response.content.decode('utf-8'))
