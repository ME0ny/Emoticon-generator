from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class Login(BaseModel):
    login: str 
    password: str