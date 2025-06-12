from datetime import datetime, timezone
from typing import List

from ..data.user_repository import UserRepository
from ...models.user import User
from ...models.watchlist import Entry

from ..projection.projection import add_favorite


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

    @staticmethod
    def get_user_watchlist(user_id: int) -> List[Entry]:
        """Service method to fetch all user watchlist entries."""
        try:
            watchlist = UserRepository.get_user_watchlist(user_id)

            entry_list = [Entry(**{**entry, "entry_id": entry.pop("id")}) for entry in watchlist]  # Noqa: E501

            return entry_list

        except Exception as e:
            print(f"Service error: {e}")

            return [
                Entry(
                   entry_id=0,
                   user_id=0,
                   anime_id=0,
                   episodes_watched=0,
                   completed=0,
                   last_updated=datetime.now(timezone.utc)
                )
            ]

    @staticmethod
    async def user_favorited_event(event: dict):
        if event["event_type"] == "AnimeFavorited":
            add_favorite(event["user_id"], event["anime_id"])
            print(f"[APPLIED] User {event['user_id']} favorited anime {event['anime_id']}")  # Noqa: E501
