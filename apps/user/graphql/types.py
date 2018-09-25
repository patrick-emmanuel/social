import graphene


class UserInput(graphene.InputObjectType):
    email = graphene.String(required=True)
    username = graphene.String(required=True)
    password = graphene.String(required=True)
