from strawberry_django_plus import gql

from ProjectAlteian.user.models import User
from ProjectAlteian.shared.utils import inject_all_fields
from ProjectAlteian.user.graphql.filters import UserFilter
from ProjectAlteian.user.graphql.orders import UserOrder

@gql.django.type(
    User, 
    filters=UserFilter, 
    order=UserOrder, 
    )
@inject_all_fields(User)
class UserType(gql.relay.Node):
    ...
