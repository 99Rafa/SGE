#pylint: disable=no-member
"""Users tests"""

# Api
from rest_framework import status
from rest_framework.test import APITestCase

# Models
from users.models import User
from rest_framework.authtoken.models import Token


class LoginTestCase(APITestCase):
    
    login_path = '/user/token/login/'

    def setUp(self):
        self.User = User.objects.create_user(
            username='test-user',
            password='super-secure-password',
        )

    def test_login(self):
        data = {
            'username': 'test-user',
            'password': 'super-secure-password'
        }
        response = self.client.post(
            path=self.login_path,
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_bad_username(self):
        data = {
            'username': 'user',
            'password': 'password'
        }
        response = self.client.post(
            path=self.login_path,
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ProfileTestCase(APITestCase):

    profile_path = '/user/test-user/'

    def setUp(self):
        self.user = User.objects.create_user(
            username='test-user',
            password='super-secure-password',
        )
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'TOKEN {self.token}')

    def test_profile_view_authenticated(self):
        response = self.client.get(self.profile_path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_view_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.profile_path)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)