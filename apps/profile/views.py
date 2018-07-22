from rest_framework import mixins, status, permissions
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.profile.models import Profile
from apps.profile.serializers import ProfileSerializer, ProfileImageSerializer


class ProfileViewSet(mixins.CreateModelMixin,
                     GenericViewSet):
    serializer_class = ProfileSerializer
    lookup_field = 'pk'
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(user=user)

    def get(self, pk):
        profile = Profile.core_objects.first_by_user(user=self.request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # handles create and update
    def create(self, request, *args, **kwargs):
        profile = Profile.core_objects.first_by_user(self.request.user)
        if profile is None:
            return super(ProfileViewSet, self).create(request, *args, **kwargs)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.update(profile, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        user = self.request.user
        profile_data = serializer.validated_data
        Profile.objects.create(user=user, **profile_data)


class ProfilePhotoViewSet(mixins.CreateModelMixin,
                          GenericViewSet):
    serializer_class = ProfileImageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        user_profile = Profile.core_objects.first_by_user(self.request.user)
        return serializer.save(profile=user_profile)
