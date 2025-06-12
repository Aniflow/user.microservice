from collections import defaultdict
from typing import Dict, List

anime_favorites: Dict[str, List[str]] = defaultdict(list)


def add_favorite(user_id: str, anime_id: str):
    if anime_id not in anime_favorites[user_id]:
        anime_favorites[user_id].append(anime_id)


def get_favorites(user_id: str) -> List[str]:
    return anime_favorites.get(user_id, [])
