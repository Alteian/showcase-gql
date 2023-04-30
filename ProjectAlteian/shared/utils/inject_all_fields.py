from strawberry_django_plus import gql
from functools import wraps

def inject_all_fields(model):
    """
    Lazy field injection for models.\n
    Example:
    >>> @gql.django.type(model=DjangoModel)\n
    >>> @inject_all_fields(DjangoModel)\n
    >>> class DjangoType:
    >>>    ...
    """
    @wraps(model)
    def wrapper(fn):
        for f in model._meta.fields:
            fn.__annotations__[f.name] = gql.auto
        return fn
    return wrapper
