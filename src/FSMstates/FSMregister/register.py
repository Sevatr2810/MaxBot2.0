from maxapi import Router, F
from maxapi.types import Command, MessageCreated, MessageCallback
from maxapi.context import MemoryContext

from FSMstates.user import user_Form
from keyboards.register import get_register_menu

register_router = Router()


@register_router.message_created(Command("register"))
async def register_handler(event: MessageCreated, context: MemoryContext):
    max_id = event.from_user.user_id

    await context.update_data(max_id=max_id)
    await context.set_state(user_Form.first_name)

    await event.message.answer(
        "Введите ваше имя"
    )


@register_router.message_created(user_Form.first_name)
async def first_name_handler(event: MessageCreated, context: MemoryContext):
    await context.update_data(first_name=event.message.body.text)
    await context.set_state(user_Form.last_name)
    await event.message.answer("Введите вашу фамилию")


@register_router.message_created(user_Form.last_name)
async def last_name_handler(event: MessageCreated, context: MemoryContext):
    await context.update_data(last_name=event.message.body.text)

    data = await context.get_data()

    await event.message.answer(
        f"Проверьте данные:\n\n"
        f"🆔 ID: {data['max_id']}\n"
        f"👤 Имя: {data['first_name']}\n"
        f"👥 Фамилия: {data['last_name']}", attachments=[get_register_menu()]
    )

    # Сохраняем в БД
    #
    # await user_repo.create_user(
    #     max_id=data["max_id"],
    #     first_name=data["first_name"],
    #     last_name=data["last_name"]
    # )

    await context.clear()


@register_router.message_callback(F.callback.payload == "confirm")
async def confirm_handler(event: MessageCallback, context: MemoryContext):
    await context.clear()
    await context.set_state(None)
    await event.message.answer("Данные отправлены на подтверждение")
    return event

@register_router.message_callback(F.callback.payload == "cancel")
async def cancel_handler(event: MessageCallback, context: MemoryContext):
    await context.clear()
    await context.set_state(None)
    await event.message.answer("Регистрация отменена")
    return event
