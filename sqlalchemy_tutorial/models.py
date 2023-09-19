from pydantic import BaseModel, ConfigDict
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Song(BaseModel):
    name: str
    artist: str


class SongWithID(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    artist: str


class Base(DeclarativeBase):
    ...


class SongDataBase(Base):
    __tablename__ = "song"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    artist: Mapped[str] = mapped_column(String(30))
