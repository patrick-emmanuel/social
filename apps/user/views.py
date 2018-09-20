# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics, permissions

from apps.user.models import User
from apps.user.serializers import UserCreateUpdateSerializer, UserRetrieveSerializer, UserListSerializer


# Create your views here


class UserListView(generics.ListAPIView):
    queryset = User.users.all()
    serializer_class = UserListSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.users.all()
    serializer_class = UserRetrieveSerializer
    lookup_field = 'username'


class UserCreateView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.users.all()
    serializer_class = UserCreateUpdateSerializer
    lookup_field = 'username'


