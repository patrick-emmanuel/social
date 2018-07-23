from django.contrib.auth.models import Group
from rest_framework.test import APIClient

from apps.user.models import User
from bionic.auth import JWTSerializer


def get_authenticated_api_client():
    client = APIClient()
    Group.objects.get_or_create(name='user')
    extra_args = {
        'username': 'bionic'
    }
    User.objects.create_user(email="inem.patrick@gmail.com", password="password", **extra_args)
    serializer = JWTSerializer()
    attrs = {
        'username_or_email': 'inem.patrick@gmail.com',
        'password': 'password',
    }
    user_credential = serializer.validate(attrs)
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + user_credential.get('token'))
    return client

