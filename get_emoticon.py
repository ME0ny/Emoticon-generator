import requests 
from typing import Optional
from functools import lru_cache
import time
import random

@lru_cache(maxsize=128)
def http_requests(data: str):
    app_responce = requests.get("http://13.59.189.236/monster/" + data)
    my_responce = {"status": app_responce.status_code}
    if my_responce["status"] == 200:
        my_responce["img"] = app_responce.content
    else:
        my_responce["img"] = ""
    return (my_responce)
