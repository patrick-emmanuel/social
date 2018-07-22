from django.db import models
# from apps.address.models import Address

# Create your models here
from ..core.models import CoreModel
from ..user.models import User
from ..profile.managers import ProfileManager
from versatileimagefield.fields import VersatileImageField, PPOIField

from .managers import ProfileImageManager


class Profile(CoreModel):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    objects = ProfileManager()


class ProfileImage(models.Model):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        null=False,
    )
    image = VersatileImageField('Headshot', upload_to='profile_images', ppoi_field='ppoi', blank=False)
    ppoi = PPOIField()
    objects = ProfileImageManager()
