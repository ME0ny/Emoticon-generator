from fastapi import APIRouter, Depends
from repositories.users import UserRepository
from models.user import User, UserIn
from .depends import get_user_repository

router = APIRouter()

@router.post("/", response_model=User)
async def create(
    user: UserIn,
    users: UserRepository = Depends(get_user_repository)):
    return await users.create(u=user)