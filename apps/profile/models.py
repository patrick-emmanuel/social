from django.db import models
# from apps.address.models import Address

# Create your models here
from apps.user.models import User
from apps.profile.managers import ProfileManager


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    date_of_birth = models.DateField()
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )

    objects = ProfileManager()
