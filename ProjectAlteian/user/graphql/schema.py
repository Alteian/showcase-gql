from strawberry.tools import merge_types

from .queries import PingQuery


UserQueries = merge_types(PingQuery)