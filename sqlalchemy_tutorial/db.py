import os
from typing import Any, AsyncContextManager, AsyncIterable, Final, Generator, Iterator
from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import AsyncEngine, async_session
from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine, SQLModel, Session
from sqlmodel.ext.asyncio.session import AsyncSession

DATABASE_URL: str | None = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise Exception("Environment variable DATABASE_URL not found")

engine: AsyncEngine = AsyncEngine(create_engine(DATABASE_URL, echo=True))


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncIterable[AsyncSession]:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session
