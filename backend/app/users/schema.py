from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    email: EmailStr

class UserCreate(User):
    role: str

class UserResponse(User):
    pass