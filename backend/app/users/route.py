# Third party
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
# Local modules
from app.core.dependencies import get_db
from app.users import schema, model

router = APIRouter(
    prefix="/signup",
    tags=["User"]
)

@router.post("", response_model=schema.UserResponse, status_code=status.HTTP_201_CREATED)
def create_account(user_credentials: schema.UserCreate, db: Annotated[Session, Depends(get_db)]):
    user = model.User(**user_credentials.model_dump())

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


