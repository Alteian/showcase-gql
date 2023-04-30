from strawberry.django.context import StrawberryDjangoContext
from functools import cached_property


class Context(StrawberryDjangoContext):
    """
    Fill in your custom context here
    """
    """
    @cached_property
    def user(self): -> typing.Optional[User]:
        if not self.request:
            return None
        authorization = self.request.headers.get("Authorization", None)
        if not authorization:
            return AnonymousUser()
        decoded = jwt.decode(authorization[7:], settings.SECRET_KEY, algorithms=[...])
        try:
            user = User.objects.get(id=decoded["id"])
        except User.DoesNotExist:
            ...
        return user
    """
