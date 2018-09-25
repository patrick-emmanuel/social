import graphene
from graphene.relay import ClientIDMutation

from .types import UserInput
from ..models import User
from .schema import UserNode


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
