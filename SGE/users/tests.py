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
