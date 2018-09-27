import graphene
import graphql_jwt

from apps.user.graphql import schema as user_schema
from apps.user.graphql.mutations import UserCreate, UserUpdate


class RootNode:
    node = graphene.Node.Field()


class Query(user_schema.Query, RootNode, graphene.ObjectType):
    pass


class Mutations(graphene.ObjectType):
    # Auth
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    # User
    user_create = UserCreate.Field()
    user_update = UserUpdate.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
