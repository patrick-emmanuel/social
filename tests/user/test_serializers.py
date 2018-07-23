from django.contrib.auth.models import Group
from django.test import TestCase

from apps.user.models import User
from apps.user.serializers import UserCreateUpdateSerializer


class UserCreateUpdateSerializerTest(TestCase):

    def setUp(self):
        extra_args = {
            'username': 'username'
        }
        Group.objects.get_or_create(name='user')
        self.user = User.objects.create_user(email="some@email.com", password="password", **extra_args)
        self.serializer = UserCreateUpdateSerializer(instance=self.user)

        self.serializer_data = {
            'email': 'some@email.com',
            'username': 'username',
            'password': 'password',
        }

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'email', 'username', 'password'})

    def test_username_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['username'], self.serializer_data['username'])

    def test_email_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['email'], self.serializer_data['email'])

    def test_password_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['password'], self.user.password)

    def test_wrong_email_format_is_valid_should_return_false(self):
        self.serializer_data['email'] = 'some@email'
        self.serializer_data['username'] = 'another_username'

        serializer = UserCreateUpdateSerializer(data=self.serializer_data)

        self.assertFalse(serializer.is_valid())

    def test_wrong_email_format_is_valid_should_return_errors_on_email(self):
        self.serializer_data['email'] = 'some@email'
        self.serializer_data['username'] = 'another_username'

        serializer = UserCreateUpdateSerializer(data=self.serializer_data)
        serializer.is_valid()

        self.assertEqual(set(serializer.errors), {'email'})

    def test_wrong_email_format_is_valid_should_return_error_message(self):
        self.serializer_data['email'] = 'some@email'
        self.serializer_data['username'] = 'another_username'

        serializer = UserCreateUpdateSerializer(data=self.serializer_data)
        serializer.is_valid()

        self.assertEqual(serializer.errors['email'][0], 'Enter a valid email address.')

    def test_duplicate_username_should_return_error(self):
        self.serializer_data['email'] = 'another@email.com'
        self.serializer_data['username'] = 'username'

        serializer = UserCreateUpdateSerializer(data=self.serializer_data)
        serializer.is_valid()

        self.assertEqual(set(serializer.errors), {'username'})

    def test_duplicate_username_should_return_error_message(self):
        self.serializer_data['email'] = 'another@email.com'
        self.serializer_data['username'] = 'username'

        serializer = UserCreateUpdateSerializer(data=self.serializer_data)
        serializer.is_valid()

        self.assertEqual(serializer.errors['username'][0], 'user with this username already exists.')
