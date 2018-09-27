import graphene
from django.contrib.auth import get_user_model

from apps.core.graphql.mutation import ModelMutation


class UserInput(graphene.InputObjectType):
    email = graphene.String(
        description="The email of the user to create")
    username = graphene.String(
        description="The username of the user to create")
    password = graphene.String(
        description="The password of the user to create")


class UserCreate(ModelMutation):
    class Arguments:
        input = UserInput(required=True)

    class Meta:
        description = 'Creates a new user.'
        model = get_user_model()


class UserUpdate(ModelMutation):
    class Arguments:
        id = graphene.ID(
            required=True, description='ID of a user to update.')
        input = UserInput(
            required=True,
            description='Fields required to update a user.')

    class Meta:
        description = 'Updates a user.'
        model = get_user_model()

    @classmethod
    def save(cls, info, instance, cleaned_input):
        instance.email = cleaned_input.get('email', instance.email)
        instance.username = cleaned_input.get('username', instance.username)
        password = cleaned_input.get('password')
        if password is not None:
            instance.set_password(password)
        instance.save()
