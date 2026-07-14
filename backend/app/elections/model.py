# Third Party
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, timedelta
# Local module
from app.db.base import Base

class Election(Base):
    __tablename__ = "elections"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    start_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime, nullable=False) 
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)