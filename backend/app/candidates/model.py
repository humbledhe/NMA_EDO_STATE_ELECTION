# Third Party
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
# Local modules
from app.db.base import Base

class Candidate(Base):
    __tablename__ = "candidates"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    position_id: Mapped[int] = mapped_column(ForeignKey("positions.id", ondelete="CASCADE"), nullable=False)