from apps.core.graphql.utils import filter_by_query_param
from apps.user import models


USER_SEARCH_FIELDS = ('email',)


def resolve_users(info, query):
    qs = models.User.objects.all()
    return filter_by_query_param(
        queryset=qs, query=query, search_fields=USER_SEARCH_FIELDS)
