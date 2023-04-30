import strawberry

from ProjectAlteian.user.graphql.types import UserType


@strawberry.type
class RegisterSuccess:
    message: str
    user: UserType


@strawberry.type
class RegisterError:
    message: str

RegisterPayload = strawberry.union(
    "RegisterPayload", 
    [RegisterSuccess, RegisterError]
    )
