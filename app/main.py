import asyncio
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import CONFIG
from .core.messaging.kafka_consumer import kafka_consume
from .routers.user_router import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(kafka_consume())
    yield
    task.cancel()

app = FastAPI(lifespan=lifespan, title="Aniflow Anime Microservice")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[CONFIG.ALLOW_ORIGINS],
    allow_methods=[CONFIG.ALLOW_METHODS],
    allow_headers=[CONFIG.ALLOW_HEADERS],
    allow_credentials=CONFIG.ALLOW_CREDENTIALS,
)

app.include_router(user_router)


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
