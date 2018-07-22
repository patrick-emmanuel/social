from django.db import models


class ProfileQuerySet(models.query.QuerySet):
    pass


class ProfileManager(models.Manager):
    pass


class ProfileImageManager(models.Manager):
    pass
