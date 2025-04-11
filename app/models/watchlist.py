from datetime import datetime

from pydantic import BaseModel


class Entry(BaseModel):
    entry_id: int
    user_id: int
    anime_id: int
    episodes_watched: int
    completed: bool
    last_updated: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
