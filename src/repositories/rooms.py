from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.rooms import Room

class RoomRepo:
    def __init__(self, session: AsyncSession):
        self.__session = session

    async def get_list(self):
        statement = select(Room).order_by(Room.name)
        result = await self.__session.scalars(statement)
        return result.all()
    
    async def get_by_id(self, room_id: int):
        statement = select(Room).where(Room.id == room_id)
        return await self.__session.scalar(statement)