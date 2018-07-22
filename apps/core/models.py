from django.db import models

# Create your models here.
from apps.core.manager import CoreManager


class CoreModel(models.Model):

    core_objects = CoreManager()

    class Meta:
        abstract = True

