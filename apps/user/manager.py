from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Group
from django.db import models


class UserQuerySet(models.QuerySet):
    pass


class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email or not password:
            raise ValueError('The email and password must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        group = Group.objects.get(name='user')
        user.save()
        user.groups.add(group)
        return user
