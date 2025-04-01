import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import CONFIG
from .routers.favorites_router import router as favorites_router
from .routers.user_router import router as user_router
from .routers.watchlist_router import router as watchlist_router

app = FastAPI(title="Aniflow Anime Microservice")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[CONFIG.ALLOW_ORIGINS],
    allow_methods=[CONFIG.ALLOW_METHODS],
    allow_headers=[CONFIG.ALLOW_HEADERS],
    allow_credentials=CONFIG.ALLOW_CREDENTIALS,
)

app.include_router(favorites_router)
app.include_router(user_router)
app.include_router(watchlist_router)


@app.get("/")
async def root():
    return {"message": "Anime microservice is running"}


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=CONFIG.API_HOST,
        port=CONFIG.API_PORT,
        reload=True
    )
