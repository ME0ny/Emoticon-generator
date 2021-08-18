from .base import BaseRepository
from db.users import users
from typing import List, Optional
from models.user import User, UserIn
from core.security import hashed_password

class UserRepository(BaseRepository):
    
    async def get_all(self, limit: int = 100, skip: int = 0) -> List[User]:
        query = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)
    
    async def get_by_id(self, id: int) -> Optional[User]:
        query = users.select().where(users.c.id==id)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def get_by_login(self, login: str) -> User:
        query = users.select().where(users.c.login==login)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def create(self, u: UserIn) -> Optional[User]:
        user = User(
            login=u.login,  
            hashed_password=hashed_password(u.password),
        )
        values = {**user.dict()}
        if (await self.get_by_login(values["login"])) is None:
            values.pop("id", None)
            query = users.insert().values(**values)
            user.id =  await self.database.execute(query)
            return user
        return None