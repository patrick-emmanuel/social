import graphene
import graphql_jwt
import apps.user.graphql.schema
from apps.user.graphql.mutations import CreateUser


class Query(apps.user.graphql.schema.Query, graphene.ObjectType):
    pass


class Mutations(graphene.ObjectType):
    # Auth
    token_auth = graphql_jwt.relay.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.relay.Verify.Field()
    refresh_token = graphql_jwt.relay.Refresh.Field()

    # User
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
