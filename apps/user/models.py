# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import Group
from django.db import models

from apps.user.manager import UserManager


# Create your models here.


class User(AbstractBaseUser):
    uid = models.UUIDField(
        unique=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name='Public identifier',
    )
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(null=False, max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    groups = models.ManyToManyField(Group)

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name_plural = "users"

    def __unicode__(self):
        return "{}".format(self.uid)

    def __str__(self):
        return "{} {}".format(self.username, self.email)

    users = UserManager()
    objects = UserManager()
