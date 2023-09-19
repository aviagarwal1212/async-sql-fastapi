import logging

from fastapi import Depends, FastAPI, Header, Response, status
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Session, select
from sqlalchemy_tutorial.db import get_session, init_db
from sqlalchemy_tutorial.models import SongModel, Song

app = FastAPI()


@app.on_event("startup")
async def on_startup() -> None:
    try:
        await init_db()
        logging.warning("Database successfully initialized")
    except Exception as e:
        logging.error("Database initialization failed")
        raise e


@app.get("/ping")
async def pong() -> dict:
    return {"ping": "pong!"}


@app.get("/songs")
async def get_songs(session: AsyncSession = Depends(get_session)) -> list[Song]:
    result = await session.execute(select(Song))
    songs: list[Song] = result.scalars().all()
    return songs


@app.post("/songs")
async def add_song(
    song: SongModel, session: AsyncSession = Depends(get_session)
) -> Response:
    song_entry = Song(**song.dict())
    session.add(song_entry)
    await session.commit()
    await session.refresh(song_entry)
    return Response(status_code=status.HTTP_200_OK)
