from datetime import datetime, timezone

from ..data.user_repository import UserRepository
from ...models.user import User


class UserService:
    """Handles business logic related to users."""

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        """Service method to get anime by ID."""
        try:
            user = UserRepository.get_user_by_id(user_id)

            print("Succesfully got userdata")

            if user:
                user["user_id"] = user.pop("id")

                return User(**user)
            else:
                print(f"Service: User with ID {user_id} not found.")

                return User(
                    user_id=0,
                    username="User not found",
                    created_at=datetime.now(timezone.utc)
                )

        except Exception as e:
            print(f"Service error: {e}")

            return User(
                user_id=0,
                username="Service error",
                created_at=datetime.now(timezone.utc)
            )
