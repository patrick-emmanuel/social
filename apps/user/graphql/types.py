from django.contrib.auth import get_user_model
from graphene import relay

from apps.core.graphql.common import CountableDjangoObjectType


class User(CountableDjangoObjectType):
    class Meta:
        model = get_user_model()
        filter_fields = ('is_active',)
        interfaces = (relay.Node,)
