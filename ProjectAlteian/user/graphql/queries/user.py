import typing
from strawberry_django_plus import gql

from ProjectAlteian.user.graphql.types import UserType

@gql.type
class UserQuery:
    user: typing.Optional[UserType] = gql.django.node()
    user_connections: gql.relay.Connection[UserType] = gql.django.connection()
