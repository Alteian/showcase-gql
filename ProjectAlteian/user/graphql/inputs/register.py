import strawberry
import typing


@strawberry.input
class RegisterInput:
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
    is_staff: typing.Optional[bool] = False
    is_superuser: typing.Optional[bool] = False
    is_active: typing.Optional[bool] = True
