from typing import List

from fastapi import APIRouter, HTTPException

from ..models.user import User
from ..models.favorite import Favorite
from ..models.watchlist import Entry
from ..models.request import FavoriteRequest
from ..core.services.user_service import UserService

router = APIRouter()


@router.get("/user/{user_id}", response_model=User)
async def get_user_by_id(user_id: int):
    return UserService.get_user_by_id(user_id)


@router.get("/user/{user_id}/favorites", response_model=List[Favorite])
async def get_user_favorites(user_id: int):
    return UserService.get_user_favorites(user_id)


@router.get("/user/{user_id}/watchlist", response_model=List[Entry])
async def get_user_watchlist(user_id: int):
    return UserService.get_user_watchlist(user_id)


@router.post("favorite")
async def favorite_anime(request: FavoriteRequest):
    try:
        UserService.add_anime_favorite(request.user_id, request.anime_id)
        return {"message": "Anime successfully favorited"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
