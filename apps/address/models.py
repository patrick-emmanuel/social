from django.db import models
import uuid

# Create your models here.
from apps.address.managers import AddressManager
from apps.user.models import User


class Address(models.Model):
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name='Public identifier',
    )
    street = models.CharField(max_length=30)
    lga = models.CharField(max_length=30)
    state = models.CharField(max_length=50)
    user = models.ManyToManyField(User)

    objects = AddressManager()

    def __str__(self):
        return "{} {} {}".format(self.street, self.lga, self.state)
