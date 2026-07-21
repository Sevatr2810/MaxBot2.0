
from maxapi.filters.middleware import BaseMiddleware
from maxapi.types import MessageCreated as Message
from typing import Any, Awaitable, Callable, Dict

from repositories.rooms import RoomRepo
from repositories.user import UserRepo

class DatabaseSessionMiddleware(BaseMiddleware):
    def __init__(self, session_maker) -> None:
        self.session_maker = session_maker

    async def __call__ (
    self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    )-> Any:
        async with self.session_maker() as session:
            data["user_repo"] = UserRepo(session=session)
            data["room_repo"] = RoomRepo(session=session)
            # print(data)

            return await handler(event, data)
