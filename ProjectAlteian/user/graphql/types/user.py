from strawberry_django_plus import gql
from strawberry.types import Info

from django.db.models.query import QuerySet

from ProjectAlteian.user.models import User
from ProjectAlteian.shared.utils import inject_all_fields
from ProjectAlteian.user.graphql.filters import UserFilter
from ProjectAlteian.user.graphql.orders import UserOrder


@gql.django.type(
    User, 
    filters=UserFilter, 
    order=UserOrder,
    pagination=True,
    )
@inject_all_fields(User, ignore_fields=["password", "id"])
class UserType(gql.relay.Node):
    id: gql.relay.GlobalID
    ...

    @classmethod
    def get_queryset(
        cls,
        queryset: QuerySet[User],
        info: Info,
        **kwargs,
        ) -> QuerySet[User]:
        queryset.filter(is_active=True)
        return queryset
