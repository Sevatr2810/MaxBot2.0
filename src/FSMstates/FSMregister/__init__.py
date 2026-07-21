from maxapi import Dispatcher

from FSMstates.FSMregister.register import register_router

def register_FSMhandlers(dp: Dispatcher):
    dp.include_routers(register_router)

