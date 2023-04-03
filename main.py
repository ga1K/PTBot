import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)  # Включаем логирование, чтобы не пропустить важные сообщения

bot = Bot(token = '5734387053:AAE_C1Ol4pqMSL7IqbzRo4H1Ey0IcwETusI')

dp = Dispatcher(bot)

@dp.message_handler(commands = ["привет", "хай"])
async def cmd_start(message: types.message):
    await message.answer("Hello!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)