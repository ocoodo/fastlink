from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    create_async_engine, 
    async_sessionmaker, 
    AsyncSession 
)


from fastapi import Depends
from typing import Annotated


engine = create_async_engine("sqlite+aiosqlite:///db.sqlite")
new_session = async_sessionmaker(
    engine, expire_on_commit=False
)

class Model(DeclarativeBase):
    pass

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def get_db_session():
    async with new_session() as session:
        yield session

DbSession = Annotated[AsyncSession, Depends(get_db_session)]