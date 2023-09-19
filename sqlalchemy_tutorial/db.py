import os
from typing import AsyncIterable

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession

DATABASE_URL: str | None = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise Exception("Environment variable DATABASE_URL not found")

engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=True)


async def get_session() -> AsyncIterable[AsyncSession]:
    async with AsyncSession(engine) as session:
        yield session
