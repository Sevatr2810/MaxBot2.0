from datetime import datetime

from maxapi.filters.middleware import BaseMiddleware
from typing import Any, Awaitable, Callable, Dict

class LoggingMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event_object: Any,
        data: Dict[str, Any],
    ) -> Any:

        time = datetime.now().strftime("%H:%M:%S")

        user = None
        action = None

        # Пользователь обычного сообщения
        if hasattr(event_object, "from_user"):
            user = event_object.from_user

        # Пользователь callback-кнопки
        elif hasattr(event_object, "callback"):
            user = event_object.callback.user

        if user:

            # Нажатие кнопки
            if hasattr(event_object, "callback"):
                action = (
                    f"нажал кнопку "
                    f"'{event_object.callback.payload}'"
                )

            # Сообщение
            elif hasattr(event_object, "message"):
                text = event_object.message.body.text
                action = f"отправил сообщение '{text}'"

        print("=" * 50)

        print(f"🕒 Время: {time}")

        if user:
            print(
                f"👤 Пользователь: {user.first_name} "
                f"(id={user.user_id})"
            )

        if action:
            print(f"⚡ Действие: {action}")

        print(
            f"📦 Событие: {event_object.update_type}"
        )

        print("=" * 50)


        return await handler(event_object, data)