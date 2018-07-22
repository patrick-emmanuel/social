from django.db import models


class CoreQuerySet(models.query.QuerySet):

    def by_user(self, user):
        return self.filter(user=user)


class CoreManager(models.Manager):
    def get_query_set(self):
        return CoreQuerySet(self.model, using=self._db)

    def first_by_user(self, user):
        result = self.get_query_set().by_user(user)
        return result[0] if len(result) > 0 else None

