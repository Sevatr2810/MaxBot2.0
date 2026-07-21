from maxapi import Dispatcher

from handlers.start import start_route

def register_handlers(dp: Dispatcher):
    dp.include_routers(start_route)