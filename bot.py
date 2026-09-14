"""
bot.py - Asosiy ishga tushirish fayli.
Telegram botini ishga tushirish, handlerlarni ulash va xatoliklarni qayd etish.
"""

import asyncio
import logging
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

from config import BOT_TOKEN, validate_config
from handlers.commands import router as commands_router
from handlers.mbti_quiz import router as mbti_router
from handlers.career_quiz import router as career_router
from handlers.growth import router as growth_router
from handlers.chat import router as chat_router

# Loglarni sozlash
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("MentorPsychologistBot")

async def main():
    # 1. Sozlamalarni tekshirish
    warnings = validate_config()
    for w in warnings:
        logger.warning(w)

    if not BOT_TOKEN:
        logger.error(
            "\n"
            "==============================================================\n"
            "XATOLIK: BOT_TOKEN topilmadi!\n"
            "Iltimos, '.env' faylini oching va Telegram @BotFather'dan olgan\n"
            "bot tokeningizni quyidagicha yozing:\n"
            "BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz\n"
            "=============================================================="
        )
        return

    # 2. Bot va Dispatcher yaratish (FSM xotirasi bilan)
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
    )
    dp = Dispatcher(storage=MemoryStorage())

    # 3. Routerlarni tartib bilan ro'yxatdan o'tkazish
    dp.include_router(commands_router)
    dp.include_router(mbti_router)
    dp.include_router(career_router)
    dp.include_router(growth_router)
    dp.include_router(chat_router)

    # 4. Eski o'qilmagan xabarlarni tozalash (drop pending updates)
    await bot.delete_webhook(drop_pending_updates=True)

    bot_info = await bot.get_me()
    logger.info(f"Bot muvaffaqiyatli ishga tushdi: @{bot_info.username} ({bot_info.full_name})")

    # Telegram rasmiy Menu tugmasini sozlash
    try:
        commands = [
            BotCommand(command="menu", description="📍 Asosiy menyu va bo'limlar"),
            BotCommand(command="mbti", description="🧠 Xarakter testi (MBTI)"),
            BotCommand(command="kasb", description="💼 Kasb tanlash testi"),
            BotCommand(command="rivojlanish", description="🌱 Shaxsiy rivojlanish"),
            BotCommand(command="tahlil", description="🔍 Vaziyat tahlili va prognoz"),
            BotCommand(command="falsafa", description="📜 Falsafiy mushohada"),
            BotCommand(command="qaror", description="🧭 Qaror qabul qilish"),
            BotCommand(command="yangi", description="🧹 Yangi suhbat boshlash"),
            BotCommand(command="help", description="ℹ️ Yordam va qo'llanma"),
        ]
        await bot.set_my_commands(commands)
        logger.info("Telegram rasmiy komandalar menyusi muvaffaqiyatli o'rnatildi.")
    except Exception as e:
        logger.warning(f"Komandalar menyusini o'rnatishda xatolik: {e}")

    logger.info("Bot xabarlarni qabul qilishga tayyor...")

    # 5. Polling rejimida botni yurgazish
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        logger.info("Bot to'xtatildi.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot dasturi foydalanuvchi tomonidan to'xtatildi.")
