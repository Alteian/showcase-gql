import strawberry
import typing

from strawberry import Info
from ProjectAlteian.user.graphql.types import UserType
from graphql.error import GraphQLError


@strawberry.type
class ContextUserQuery:

    @strawberry.field
    def context_user(self, info: Info) -> UserType:
        if info.context.user.is_anonymous:
            raise GraphQLError("Not logged in!")
        return typing.cast(UserType, info.context.user)
