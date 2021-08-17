from fastapi import APIRouter, Depends, HTTPException, status
from models.user import User
from .depends import get_current_user
from fastapi.responses import StreamingResponse
from repositories.emoticon import emoticon_request

router = APIRouter()

@router.get("/")
def get_emoticon(
    current_user: User = Depends(get_current_user),
    name: str = ""):
    img = emoticon_request(name)
    if img:
        return StreamingResponse(img, media_type="image/png")
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    