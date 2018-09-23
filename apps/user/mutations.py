import graphene
from graphene.relay import ClientIDMutation
from apps.user.models import User
from apps.user.schema import UserNode


class UserInput(graphene.InputObjectType):
    email = graphene.String(required=True)
    username = graphene.String(required=True)
    password = graphene.String(required=True)


class CreateUser(ClientIDMutation):
    class Input:
        user = graphene.Argument(UserInput)
    new_user = graphene.Field(UserNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        user_data = input['user']
        user = User.objects.create_user(
            email=user_data.pop('email'),
            password=user_data.pop('password'),
            **user_data
        )
        return cls(new_user=user)
