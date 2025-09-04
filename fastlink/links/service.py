from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from typing import Optional

from .models import Link
from .utils import generate_short_code


async def new_link(
    db_session: AsyncSession, 
    target_url: str
) -> Link:
    link = Link(target_url=target_url)
    db_session.add(link)
    await db_session.flush()
    
    short_code = generate_short_code(link.id)
    link.short_code = short_code
    await db_session.commit()
    return link


async def get_link(
    db_session: AsyncSession, 
    short_code: str
) -> Optional[Link]:
    query = await db_session.execute(
        select(Link).
        where(Link.short_code == short_code)
    )
    return query.scalar_one_or_none()
