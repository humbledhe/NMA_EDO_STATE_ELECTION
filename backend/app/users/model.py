# Third Party
from sqlalchemy import DateTime, func
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from datetime import datetime
from enum import Enum as Enum
# Local modules
from app.db.base import Base

class Role(Enum):
    ADMIN = "admin",
    VOTER = "voter",

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    role: Mapped[Role] = mapped_column(SQLEnum(Role), default=Role.VOTER, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)