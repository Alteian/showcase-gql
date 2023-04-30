import strawberry


@strawberry.type
class PingQuery:
   @strawberry.field(description="A simple ping to test the server.")
   def ping(self) -> str:
       return "pong"
