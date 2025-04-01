from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    username: str
    created_at: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
