# Third Party
from pydantic import BaseModel, ConfigDict, EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    password: str