from sqlmodel import SQLModel, Field


class SongModel(SQLModel):
    name: str
    artist: str


class Song(SQLModel, table=True):
    id: int | None = Field(default=None, nullable=False, primary_key=True)
    name: str
    artist: str
