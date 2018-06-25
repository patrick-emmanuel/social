from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "This commmand is used for creating user groups and assigning roles to the groups."

    def add_arguments(self, parser):
        parser.add_argument('group', nargs=1, type=str)
        parser.add_argument('permission', nargs=1, type=str)
        parser.add_argument('model', nargs=1, type=str)

        """
        This method creates a new group and new permission or uses the already existing
        one. Then it assigns this permission on the specified model.
        example --- python manage.py createrole group-name permission-name model-name
        """

    def handle(self, *args, **options):
        group_name = options['group'][0]
        permission_name = options['permission'][0]
        model = options['model'][0]
        new_group, created = Group.objects.get_or_create(name=group_name)
        content_type = ContentType.objects.get(model=model)
        permission, created = Permission.objects.get_or_create(codename=permission_name,
                                                               name=permission_name.replace('_', ' '),
                                                               content_type=content_type)
        new_group.permissions.add(permission)
        self.stdout.write('Successfully created group {} '
                          'with {} on model {}.', group_name, permission_name, model)


