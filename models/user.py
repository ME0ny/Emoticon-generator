from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None
    login: str
    hashed_password: str

class UserIn(BaseModel):
    login: str
    password: str


