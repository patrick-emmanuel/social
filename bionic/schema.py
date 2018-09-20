import graphene
import apps.user.schema


class Query(apps.user.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
