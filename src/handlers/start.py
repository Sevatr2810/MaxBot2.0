from maxapi import Router, F
from maxapi.types import Command, MessageCreated
from maxapi.enums.format import Format

start_route = Router()

@start_route.message_created(Command("start"))
async def start_handler(event: MessageCreated):
    await event.message.answer("Главное меню")
    return event
