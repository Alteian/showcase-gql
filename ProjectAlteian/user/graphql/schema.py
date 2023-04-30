from strawberry.tools import merge_types

from .queries import PingQuery, UserQuery
from .mutations import RegisterMutation

UserBatchQuery = merge_types(
    name="UserBatchQuery",
    types=(
        UserQuery,
        PingQuery
        )
    )


UserBatchMutation = merge_types(
    name="UserBatchMutation",
    types=(
        RegisterMutation,
        )
    )
