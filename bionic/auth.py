from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer, jwt_payload_handler, jwt_encode_handler
from apps.user.models import User


class JWTSerializer(JSONWebTokenSerializer):
    username_field = 'username_or_email'

    def validate(self, attrs):
        password = attrs.get("password")
        user_obj = User.users.filter(email=attrs.get("username_or_email")).first() or \
            User.users.filter(username=attrs.get("username_or_email")).first()
        if user_obj:
            credentials = {
                'username': user_obj.email,
                'password': password
            }
            if all(credentials.values()):
                user = authenticate(**credentials)
                if user:
                    if not user.is_active:
                        raise serializers.ValidationError('User account is disabled.')
                    payload = jwt_payload_handler(user)
                    return {
                        'token': jwt_encode_handler(payload),
                        'user': user
                    }
                else:
                    raise serializers.ValidationError('Wrong log in credentials.')
            else:
                message = "Must include {username_field} and password".format(username_field=self.username_field)
                raise serializers.ValidationError(message)
        else:
            raise serializers.ValidationError('Account with this email/username does not exists')
