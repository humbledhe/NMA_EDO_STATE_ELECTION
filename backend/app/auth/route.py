# Third Party
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import Annotated
# Local modules
from app.users import model
from app.auth import schema
from app.core.security import verify, hash, create_access_token
from app.core.dependencies import get_db

router = APIRouter(
    prefix=("/login"),
    tags=["Authentication"],
)

@router.post("")
def login_user(user_credentials: schema.UserLogin, db: Annotated[Session, Depends(get_db)]):
    user = db.query(model.User).filter(model.User.email == user_credentials.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentuals")

    hashed_password = hash(user_credentials.password)

    if not verify(user_credentials.password, hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentuals")

    access_token = create_access_token(data={
        "user_id": user.id
    })

    return {
        "access_token": access_token,
        "token_data": "bearer",
    }