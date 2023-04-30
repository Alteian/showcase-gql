import typing

from strawberry.types import Info
from strawberry_django_plus import gql
from strawberry_django_plus.optimizer import optimize
from strawberry_django.filters import apply as apply_filters
from strawberry_django.ordering import apply as apply_ordering

from ProjectAlteian.user.graphql.types import UserType
from ProjectAlteian.user.graphql.filters import UserFilter
from ProjectAlteian.user.graphql.orders import UserOrder
from ProjectAlteian.user.models import User

@gql.type
class UserQuery:
    user: typing.Optional[UserType] = gql.django.node()
    user_connections: gql.relay.Connection[UserType] = gql.django.connection()
    
    @gql.django.field()
    def user_list(
        self,
        info: Info,
        filters: typing.Optional[UserFilter] = None,
        order: typing.Optional[UserOrder] = None,
        ) -> typing.List[UserType]:
        queryset = optimize(UserType.get_queryset(User.objects.all(), info), info)
        if filters:
            queryset = apply_filters(queryset, filters)
        if order:
            queryset = apply_ordering(queryset, order)
        return queryset
