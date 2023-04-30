from strawberry_django_plus import gql

from ProjectAlteian.user.models import User
from ProjectAlteian.shared.utils import inject_all_fields


@gql.django.order(User)
@inject_all_fields(User)
class UserOrder:
    ...
