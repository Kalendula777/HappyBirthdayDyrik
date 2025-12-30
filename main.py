import asyncio
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import time
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

# ID группы 
GROUP_ID = -1002054071843

# Время отправки (24-часовой формат)
SEND_TIME = time(hour=14, minute=13)  # 10:00 утра

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def get_chat_id(message):
    print(message.chat.id)


async def send_congrats():
    await bot.send_message(
        GROUP_ID,
        "Я щас въебу вам, если ещё раз типните меня, уёбища ебаные"
    )


async def main():
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

    # Запуск каждый день в заданное время
    scheduler.add_job(
        send_congrats,
        trigger="cron",
        hour=SEND_TIME.hour,
        minute=SEND_TIME.minute
    )

    scheduler.start()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
