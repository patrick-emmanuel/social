import graphene
from graphene_django.filter import DjangoFilterConnectionField

from apps.user.graphql.resolvers import resolve_users
from apps.user.graphql.types import User


class Query:
    user = graphene.Field(
        User, id=graphene.Argument(graphene.ID),
        description='Lookup a user by ID.')
    all_users = DjangoFilterConnectionField(User)

    def resolve_user(self, info, id):
        return graphene.Node.get_node_from_global_id(info, id, User)

    def resolve_users(self, info, query=None, **kwargs):
        return resolve_users(info, query=query)
