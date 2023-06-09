from strawberry import Schema
from strawberry.tools import merge_types  # noqa
from strawberry.schema.config import StrawberryConfig
from strawberry.extensions import QueryDepthLimiter
from strawberry_django_plus.directives import SchemaDirectiveExtension
from strawberry_django_plus.optimizer import DjangoOptimizerExtension

from ProjectAlteian.user.graphql.schema import UserBatchQuery, UserBatchMutation

Query = UserBatchQuery
Mutation = UserBatchMutation

schema = Schema(
    query=Query,
    mutation=Mutation,
    # subscription=Subscription,
    config=StrawberryConfig(
        auto_camel_case=True,
    ),
    extensions=[
        QueryDepthLimiter(max_depth=10),
        SchemaDirectiveExtension,
        DjangoOptimizerExtension,
    ],
)
