from pydantic import BaseModel, EmailStr, ConfigDict

class User(BaseModel):
    username: str
    email: EmailStr

class UserCreate(User):
    password: str
    role: str

class UserResponse(User):
    model_config = ConfigDict(from_attribute=True)