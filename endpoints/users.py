from fastapi import APIRouter, Depends, HTTPException
from repositories.users import UserRepository
from models.user import User, UserIn
from .depends import get_user_repository, get_current_user
from typing import List

router = APIRouter()

@router.get("/", response_model=List[User])
async def read_users(
    users: UserRepository = Depends(get_user_repository),
    limit: int = 100, 
    skip: int = 0):
    return await users.get_all(limit=limit, skip=0)

@router.post("/", response_model=User)
async def create(
    user: UserIn,
    users: UserRepository = Depends(get_user_repository)):
    return await users.create(u=user)

@router.get("/by_login", response_model=User)
async def read_by_login(
    users: UserRepository = Depends(get_user_repository),
    current_user: User = Depends(get_current_user),
    login: str = ""):
    user = await users.get_by_login(login=login)
    if user is None or user.login != current_user.login:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found user")
    return user