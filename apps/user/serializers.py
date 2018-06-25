from rest_framework import serializers

from apps.user.models import User


class UserCreateUpdateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'uid',)

    def create(self, validated_data):
        user = User.users.create_user(
            email=validated_data.pop('email'),
            password=validated_data.pop('password'),
            **validated_data
        )
        return user


class UserRetrieveSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'email', 'username', 'uid')
        extra_kwargs = {
            'url': {'view_name': 'users:user-detail', 'lookup_field': 'username', }
        }


class UserListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'email', 'username', 'uid')
        extra_kwargs = {
            'url': {'view_name': 'users:user-detail', 'lookup_field': 'username', }
        }
