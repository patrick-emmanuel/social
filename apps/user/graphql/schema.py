from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from apps.user.models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ('uid', 'username', 'email', 'is_active',)
        interfaces = (relay.Node, )


class Query(object):
    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)
