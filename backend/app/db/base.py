from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# Import your models AFTER Base is defined
from app.users.model import User