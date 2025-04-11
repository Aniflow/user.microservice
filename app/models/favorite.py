from datetime import datetime

from pydantic import BaseModel


class Favorite(BaseModel):
    favorite_id: int
    user_id: int
    anime_id: int
    favorited_at: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
