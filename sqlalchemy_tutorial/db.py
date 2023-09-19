import os
from typing import Final, Iterator
from sqlalchemy.engine import Engine
from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL: str | None = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise Exception("Environment variable DATABASE_URL not found")

engine: Engine = create_engine(DATABASE_URL, echo=True)


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


def get_session() -> Iterator[Session]:
    with Session(engine) as session:
        yield session
