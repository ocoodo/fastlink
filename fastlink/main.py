from fastapi import FastAPI

from .database import create_tables

app = FastAPI()

# including routers
from fastlink.links.router import router as links_router
app.include_router(links_router)

@app.on_event("startup")
async def startup():
    await create_tables()
    