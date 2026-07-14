# Third Party
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
# Local modules
from app.db.base import Base

class Position(Base):
    __tablename__ = "positions"

    id: Mapped[int] = mapped_column(primary_key=True)
    election_id: Mapped[int] = mapped_column(ForeignKey("elections.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    max_votes: Mapped[int] = mapped_column(default=1)
    display_order: Mapped[int] = mapped_column(nullable=False)