from typing import List

from fastapi import APIRouter

from ..models.user import User
from ..models.watchlist import Entry
from ..core.services.user_service import UserService

router = APIRouter()


@router.get("/user/{user_id}", response_model=User)
async def get_user_by_id(user_id: int):
    return UserService.get_user_by_id(user_id)


@router.get("/user/{user_id}/watchlist", response_model=List[Entry])
async def get_user_watchlist(user_id: int):
    return UserService.get_user_watchlist(user_id)
