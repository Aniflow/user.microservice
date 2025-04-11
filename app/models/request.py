from pydantic import BaseModel


class FavoriteRequest(BaseModel):
    user_id: int
    anime_id: int
