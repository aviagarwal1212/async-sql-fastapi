from fastapi import Depends, FastAPI, Response, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy_tutorial.db import get_session
from sqlalchemy_tutorial.models import Song, SongDataBase, SongWithID

app = FastAPI()


@app.get("/ping")
async def pong() -> dict:
    return {"ping": "pong!"}


@app.get("/songs")
async def get_songs(session: AsyncSession = Depends(get_session)) -> list[SongWithID]:
    stmt = select(SongDataBase)
    result = await session.scalars(stmt)
    songs_withids = [SongWithID.model_validate(song) for song in result]
    return songs_withids


@app.post("/songs")
async def add_song(
    song: Song, session: AsyncSession = Depends(get_session)
) -> Response:
    song_entry = SongDataBase(**song.dict())
    session.add(song_entry)
    await session.commit()
    return Response(
        content="Song added to database", status_code=status.HTTP_201_CREATED
    )
