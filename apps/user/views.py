# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

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


# Endpoint for registering new users.

class UserCreateView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create(request.data)
        payload = jwt_payload_handler(user)
        response = {
            'token': jwt_encode_handler(payload),
            'user': serializer.data
        }
        return Response(response, status=status.HTTP_201_CREATED)


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.users.all()
    serializer_class = UserCreateUpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)
