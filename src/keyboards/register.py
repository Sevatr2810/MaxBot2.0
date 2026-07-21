from maxapi.utils.inline_keyboard import InlineKeyboardBuilder
from maxapi.types import CallbackButton

def get_register_menu():
    builder = InlineKeyboardBuilder()

    builder.row(
        CallbackButton(text="Отмена", payload="cancel"),
        CallbackButton(text="Подтвердить", payload="confirm")
    )

    keyboard = builder.as_markup()

    return keyboard