from .base import BaseRepository
from db.users import users
from typing import List, Optional
from models.users import User, UserIn
class UserRepository(BaseRepository):
    
    async def get_by_id(self, id: int) -> Optional[User]:
        query = users.select().where(users.c.id==id).first()
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def create(self, u: UserIn) -> User:
        user = User(
            login=u.login,  
            hashed_password=hashed_password(u.password),
        )
        values = {**user.dict()}
        values.pop("id", None)
        query = users.insert().values()
        user.id =  await self.database.execute(query)
        return user
    
    async def get_by_login(self, login: str) -> User:
        query = users.select().where(users.c.login==login).first()
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)
