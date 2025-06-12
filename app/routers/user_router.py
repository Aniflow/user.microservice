from typing import List

from fastapi import APIRouter

from ..models.user import User
from ..models.watchlist import Entry
from ..core.services.user_service import UserService
from ..core.projection.projection import get_favorites

router = APIRouter()


@router.get("/user/{user_id}", response_model=User)
async def get_user_by_id(user_id: int):
    return UserService.get_user_by_id(user_id)


@router.get("/user/{user_id}/watchlist", response_model=List[Entry])
async def get_user_watchlist(user_id: int):
    return UserService.get_user_watchlist(user_id)


@router.get("/user/{user_id}/favorites")
async def get_user_favorites(user_id: str):
    favorites = get_favorites(user_id)
    if not favorites:
        return {"user_id": user_id, "favorites": []}
    return {"user_id": user_id, "favorites": favorites}
