from rest_framework import serializers

from apps.user.models import User


class UserCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    def create(self, validated_data):
        user = User.users.create_user(
            email=validated_data.pop('email'),
            password=validated_data.pop('password'),
            **validated_data
        )
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        password = validated_data.get('password')
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


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
