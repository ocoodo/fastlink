from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from fastlink.database import DbSession
from .schemas import NewLinkRequest
from .service import new_link, get_link


router = APIRouter()


@router.post("/links/")
async def new_link_handler(
    data: NewLinkRequest,
    db_session: DbSession,
):
    target_url = str(data.target)
    link = await new_link(db_session, target_url)
    return link


@router.get("/l/{short_code}")
async def redirect_handler(
    short_code: str,
    db_session: DbSession
):
    link = await get_link(db_session, short_code)
    if not link:
        raise HTTPException(
            status_code=404,
            detail='Link not found'
        )
    return RedirectResponse(
        status_code=301,
        url=link.target_url
    )