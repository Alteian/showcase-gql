import strawberry

from strawberry.types import Info

from django.core.exceptions import ValidationError
from django.db import IntegrityError

from ProjectAlteian.user.models import User

from ProjectAlteian.user.graphql.payloads import RegisterPayload, RegisterSuccess, RegisterError
from ProjectAlteian.user.graphql.inputs import RegisterInput

@strawberry.type
class RegisterMutation:
    
    @strawberry.mutation(description="Register a new user.")
    def register(
        self,
        info: Info,
        input: RegisterInput
        ) -> RegisterPayload:
        try:
            user = User.objects.create_user(**input.__dict__)
            return RegisterSuccess(
                message="User created successfully",
                user=user
                )
        except ValidationError:
            return RegisterError(message="Invalid input")
        except IntegrityError:
            return RegisterError(message="User already exists")
        except Exception as e:
            return RegisterError(message=str(e))
