from fastapi import APIRouter

from ..models.user import User
from ..core.services.user_service import UserService

router = APIRouter()


@router.get("/user/{user_id}", response_model=User)
async def get_user_by_id(user_id: int):
    return UserService.get_user_by_id(user_id)
