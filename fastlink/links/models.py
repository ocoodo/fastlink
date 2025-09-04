from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from sqlalchemy import DateTime

from datetime import datetime

from fastlink.database import Model


class Link(Model):
    __tablename__ = 'links'
    id: Mapped[int] = mapped_column(primary_key=True)
    target_url: Mapped[str]
    short_code: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    
