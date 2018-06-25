from django.contrib.auth.models import Group
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "This command is used for creating user groups"

    def add_arguments(self, parser):
        parser.add_argument('group', nargs=1, type=str)

    def handle(self, *args, **options):
        group_name = options['group'][0]
        Group.objects.get_or_create(name=group_name)
        self.stdout.write('Successfully created group {}'.format(group_name))


