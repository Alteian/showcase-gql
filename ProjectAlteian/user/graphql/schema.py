from strawberry.tools import merge_types

from .queries import PingQuery
from .queries import UserQuery


UserBatchQuery = merge_types(
    name="UserBatchQuery",
    types=(
        UserQuery,
        PingQuery
        )
    )
