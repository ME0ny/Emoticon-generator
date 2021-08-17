from starlette.config import Config

config = Config(".env")

DATABASE_URL = config("EG_DATABASE_URL", cast=str, default="")
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("EE_SECRET_KEY", cast=str, default="482a54c5c70a20c6b0c8740b01264a6fc1ceb1debdcd741bfd526aee54cb802c")
EMOTICON_SERVER = "http://13.59.189.236/monster/"
