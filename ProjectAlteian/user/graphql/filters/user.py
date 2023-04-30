from strawberry_django_plus import gql

from ProjectAlteian.user.models import User
from ProjectAlteian.shared.utils import inject_all_fields


@gql.django.filter(User, lookups=True)
@inject_all_fields(User)
class UserFilter:
    ...
