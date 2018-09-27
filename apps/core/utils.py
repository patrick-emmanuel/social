from django.db.models import Q
from graphene_django.registry import get_global_registry
from graphql import GraphQLError
from graphql_relay import from_global_id


registry = get_global_registry()


def snake_to_camel_case(name):
    """Convert snake_case variable name to camelCase."""
    if isinstance(name, str):
        split_name = name.split('_')
        return split_name[0] + "".join(map(str.capitalize, split_name[1:]))
    return name


def get_nodes(ids, graphene_type=None):
    """Return a list of nodes.

    If the `graphene_type` argument is provided, the IDs will be validated
    against this type. If the type was not provided, it will be looked up in
    the Graphene's registry. Raises an error if not all IDs are of the same
    type.
    """
    pks = []
    types = []
    for graphql_id in ids:
        _type, _id = from_global_id(graphql_id)
        if graphene_type:
            assert str(graphene_type) == _type, (
                'Must receive an {} id.').format(graphene_type._meta.name)
        pks.append(_id)
        types.append(_type)

    # If `graphene_type` was not provided, check if all resolved types are
    # the same. This prevents from accidentally mismatching IDs of different
    # types.
    if types and not graphene_type:
        assert len(set(types)) == 1, 'Received IDs of more than one type.'
        # get type by name
        type_name = types[0]
        for model, _type in registry._registry.items():
            if _type._meta.name == type_name:
                graphene_type = _type
                break

    nodes = list(graphene_type._meta.model.objects.filter(pk__in=pks))
    if not nodes:
        raise GraphQLError(
            "Could not resolve to a nodes with the global id list of '%s'."
            % ids)
    nodes_pk_list = [str(node.pk) for node in nodes]
    for pk in pks:
        assert pk in nodes_pk_list, (
            'There is no node of type {} with pk {}'.format(_type, pk))
    return nodes


def filter_by_query_param(queryset, query, search_fields):
    """Filter queryset according to given parameters.

    Keyword arguments:
    queryset - queryset to be filtered
    query - search string
    search_fields - fields considered in filtering
    """
    if query:
        query_by = {
            '{0}__{1}'.format(
                field, 'icontains'): query for field in search_fields}
        query_objects = Q()
        for q in query_by:
            query_objects |= Q(**{q: query_by[q]})
        return queryset.filter(query_objects)
    return queryset


def update_instance(instance, clean_input):
    for key, val in clean_input:
        if hasattr(instance, key):
            setattr(instance, key, val)
