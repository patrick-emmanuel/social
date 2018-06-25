from django.contrib.auth.models import Group
from django.db import IntegrityError
from django.test import TestCase

from apps.user.models import User


class UserModelTest(TestCase):

    def setUp(self):
        extra_args = {
            'username': 'bionic'
        }
        Group.objects.get_or_create(name='user')
        self.user = User.users.create_user(email="inem.patrick@gmail.com", password="password", **extra_args)

    def test_string_representation(self):
        self.assertEqual(str(self.user), "bionic inem.patrick@gmail.com")

    def test_verbose_name_plural(self):
        self.assertEqual(str(self.user._meta.verbose_name_plural), "users")

    def test_save_without_email(self):
        self.assertRaises(ValueError, User.users.create_user, email=None, password="password")

    def test_create_user(self):
        new_user = User.users.create_user(email="patrick@gmail.com", password="password")
        self.assertEqual("patrick@gmail.com", new_user.email)

    def test_save_duplicate_email_raises_integrity_error(self):
        User.users.create_user(email="duplicate@gmail.com", password="password")
        self.assertRaises(IntegrityError, User.users.create_user, email="duplicate@gmail.com", password="password")
