from core.config import EMOTICON_SERVER
import requests
from functools import lru_cache
import io

@lru_cache(maxsize=128)
def emoticon_request(name: str):
    url = EMOTICON_SERVER + name
    r = requests.get(url)
    if r.status_code == 200:
        return io.BytesIO(r.content)
    return None