import asyncio
from maxapi.filters.middleware import BaseMiddleware
from maxapi.types import MessageCreated as Message
from maxapi.context import MemoryContext
from typing import Any, Awaitable, Callable, Dict

from FSMstates.user import user_Form


class RegisterMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        context: MemoryContext | None = data.get("context")
        user_repo = data.get("user_repo")

        if user_repo is None:
            return await handler(event, data)

        if getattr(event, "callback", None) is not None:
            return await handler(event, data)

        user = None
        if hasattr(event, "from_user") and getattr(event, "from_user", None):
            user = event.from_user
        elif hasattr(event, "callback") and getattr(event, "callback", None):
            user = event.callback.user

        if user is None:
            return await handler(event, data)

        if context is not None:
            current_state = await context.get_state()
            if current_state is not None:
                state_name = getattr(current_state, "name", None) or str(current_state)
                if state_name in {str(user_Form.first_name), str(user_Form.last_name)}:
                    return await handler(event, data)

        existing_user = await user_repo.get_user_by_max_id(user.user_id)

        if existing_user is None:
            print(f"Пользователь {user.user_id} не найден в БД")

            msg = await event.message.answer("Для начала пройдите регистрацию")
            max_id = user.user_id
            await context.update_data(max_id=max_id)
            await event.message.answer("Введите ваше имя:")
            await context.set_state(user_Form.first_name)
            await asyncio.sleep(60)
            await msg.message.delete()
            return

        return await handler(event, data)