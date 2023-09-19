import logging

from fastapi import Depends, FastAPI, Header, Response, status
from sqlalchemy.engine import Result
from sqlmodel import Session, select
from sqlalchemy_tutorial.db import get_session, init_db
from sqlalchemy_tutorial.models import SongModel, Song

app = FastAPI()


@app.on_event("startup")
def on_startup() -> None:
    try:
        init_db()
        logging.warning("Database successfully initialized")
    except Exception as e:
        logging.error("Database initialization failed")
        raise e


@app.get("/ping")
async def pong() -> dict:
    return {"ping": "pong!"}


@app.get("/songs")
def get_songs(session: Session = Depends(get_session)) -> list[Song] | None:
    songs = session.exec(select(Song)).all()
    return songs


@app.post("/songs")
def add_song(song: SongModel, session: Session = Depends(get_session)) -> Response:
    print(song)
    song_entry: Song = Song(name=song.name, artist=song.artist)
    session.add(song_entry)
    session.commit()
    session.refresh(song_entry)
    return Response(status_code=status.HTTP_200_OK)
