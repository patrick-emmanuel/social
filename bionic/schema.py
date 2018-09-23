import graphene
import graphql_jwt
import apps.user.schema
from apps.user.mutations import CreateUser


class Query(apps.user.schema.Query, graphene.ObjectType):
    pass


class Mutations(graphene.ObjectType):
    token_auth = graphql_jwt.relay.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.relay.Verify.Field()
    refresh_token = graphql_jwt.relay.Refresh.Field()
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
