from os import getenv
import asyncio
from maxapi import Bot, Dispatcher
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


from handlers import register_handlers
from FSMstates.FSMregister import register_FSMhandlers
# from callbacks import register_callbacks
from database.models import BaseModel
from middleware import register_middlewares


load_dotenv()
TOKEN = getenv("BOT_TOKEN")

async def init_model(engine):
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    engine= create_async_engine(
    url="sqlite+aiosqlite:///employees_maxbot_db.db"
    )
    session_maker = async_sessionmaker(engine, expire_on_commit=False)


    register_middlewares(dp, session_maker)
    register_handlers(dp)
    register_FSMhandlers(dp)
    # register_callbacks(dp)

    await init_model(engine)
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print ("Вы остановили бота")