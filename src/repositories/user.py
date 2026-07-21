from datetime import date

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.users import User

class UserRepo:
    def __init__(self, session: AsyncSession):
        self.__session = session

    async def get_user_by_max_id(self, max_id: int):
        statement = select(User).where(User.max_id == max_id)

        return await self.__session.scalar(statement)

    async def get_all_users_full_name(self):
        statement = select(User).order_by(User.full_name)
        result = await self.__session.scalars(statement)
        return result.all()
    
    async def get_all_users_id(self):
        statement = select(User).order_by(User.id)
        result = await self.__session.scalars(statement)
        return result.all()
    
    async def get_all_admins_id(self):
        statement = select(User).order_by(User.isAdmin)
        result = await self.__session.scalars(statement)
        return result.all()
    
    async def get_access_level_by_id(self):
        statement = select(User).order_by(User.access_level)
        result = await self.__session.scalars(statement)
        return result.all()
    
    async def change_user_max_id(self, max_id: int, new_max_id: str):
        user = await self.get_user_by_max_id(max_id=max_id)

        if user is None:
            return None
        
        user.max_id = new_max_id
        await self.__session.commit()
        return user

    async def change_user_first_name(self, max_id: int, new_name: str):
        user = await self.get_user_by_max_id(max_id=max_id)

        if user is None:
            return None
        
        user.first_name = new_name
        await self.__session.commit()
        return user
    
    async def change_user_last_name(self, max_id: int, new_last_name: str):
        user = await self.get_user_by_max_id(max_id=max_id)

        if user is None:
            return None
        
        user.last_name = new_last_name
        await self.__session.commit()
        return user
    
    async def change_user_birthday(self, max_id: int, new_birthday: date):
        user = await self.get_user_by_max_id(max_id=max_id)

        if user is None:
            return None
        
        user.birthday = new_birthday
        await self.__session.commit()
        return user
    
    async def change_user_isAdmin(self, max_id: int, isAdmin: bool):
        user = await self.get_user_by_max_id(max_id=max_id)

        if user is None:
            return None
        
        user.isAdmin = isAdmin
        await self.__session.commit()
        return user
    
    async def change_user_access_level(self, max_id: int, access_level: int):
        user = await self.get_user_by_max_id(max_id=max_id)

        if user is None:
            return None
        
        user.access_level = access_level
        await self.__session.commit()
        return user

    async def creat_or_update_user(self, max_id: int, fullname: str, username:str):
        user = await self.get_user_by_max_id(max_id)

        if not user:
            await self.create_user(max_id, fullname, username)
        else:
            user.full_name = fullname
            user.username = username

            await self.__session.commit()

    async def create_user(self, max_id: int, first_name: str, last_name: str):
        user = User(max_id=max_id, first_name=last_name, last_name=first_name)
        self.__session.add(user)