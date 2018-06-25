from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.user.models import User
from tests.helpers import get_authenticated_api_client


class UserViewsTest(TestCase):

    def setUp(self):
        self.authenticated_client = get_authenticated_api_client()

    def test_register_user_returns_201(self):
        user_json = {"email": "test@test.com", "password": "password", "username": "password"}
        response = self.authenticated_client.post(reverse('users:user-create'), user_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_user_returns_user(self):
        user_json = {"email": "test@test.com", "password": "password", "username": "password"}
        response = self.authenticated_client.post(reverse('users:user-create'), user_json, format='json')
        self.assertIsNotNone(response.data.get('user'))

    def test_register_user_returns_token(self):
        user_json = {"email": "test@test.com", "password": "password", "username": "password"}
        response = self.authenticated_client.post(reverse('users:user-create'), user_json, format='json')
        self.assertIsNotNone(response.data.get('token'))

    def test_list_all_users_returns_200(self):
        response = self.authenticated_client.get(reverse('users:user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_all_users_returns_one_user(self):
        response = self.authenticated_client.get(reverse('users:user-list'))
        self.assertEqual(len(response.data), 1)

    def test_list_all_users_returns_401(self):
        client = APIClient()
        response = client.get(reverse('users:user-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_a_user_200(self):
        user = User.users.get(username='bionic')
        response = self.authenticated_client.get(reverse('users:user-detail', args=[user.username]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
