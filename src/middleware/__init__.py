from maxapi import Dispatcher

from middleware.session import DatabaseSessionMiddleware
from middleware.loggining import LoggingMiddleware
from middleware.register import RegisterMiddleware

def register_middlewares(dp: Dispatcher, session_maker):
    dp.register_inner_middleware(DatabaseSessionMiddleware(session_maker))
    dp.register_outer_middleware(LoggingMiddleware())
    dp.register_inner_middleware(RegisterMiddleware())