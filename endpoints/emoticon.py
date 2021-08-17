from fastapi import APIRouter, Depends
from models.user import User
from .depends import get_current_user
from fastapi.responses import StreamingResponse
from core.config import EMOTICON_SERVER
import requests
import io

router = APIRouter()

@router.get("/")
async def get_emoticon(
    current_user: User = Depends(get_current_user),
    name: str = ""):
    r = requests.get(EMOTICON_SERVER + name)
    return StreamingResponse(io.BytesIO(r.content), media_type="image/png")

    