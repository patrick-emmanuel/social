def first(query):
    try:
        return query.all()[0]
    except:
        return None