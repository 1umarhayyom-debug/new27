"""
handlers/chat.py - Foydalanuvchining matnli xabarlarini qabul qilish va ularga javob berish.
Xavfsizlik filtrlari va AI integratsiyasi.
"""

import logging
from aiogram import Router, F
from aiogram.types import Message
from aiogram.enums import ChatAction
from aiogram.exceptions import TelegramBadRequest

from guardrails import check_guardrails
from ai_service import generate_response

router = Router()
logger = logging.getLogger(__name__)

@router.message(F.text)
async def handle_user_text(message: Message):
    user_text = message.text.strip()
    user_id = message.from_user.id

    # 1. Xavfsizlik va maxsus qoidalar tekshiruvi (Guardrails)
    guardrail_result = check_guardrails(user_text)
    if guardrail_result:
        response_text = guardrail_result["response"]
        try:
            await message.answer(response_text, parse_mode="Markdown")
        except TelegramBadRequest:
            await message.answer(response_text)
        return

    # 2. Foydalanuvchiga yozish holatini ko'rsatish (Typing action)
    try:
        await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
    except Exception as e:
        logger.debug(f"Chat action yuborishda xatolik: {e}")

    # 3. Sun'iy intellekt (Gemini AI) orqali chuqur tahlil va maslahat olish
    ai_reply = await generate_response(user_id=user_id, message_text=user_text)

    # 4. Javobni foydalanuvchiga yuborish
    try:
        await message.answer(ai_reply, parse_mode="Markdown")
    except TelegramBadRequest:
        # Agar Markdown belgilarida muammo bo'lsa, oddiy matn sifatida yuborish
        await message.answer(ai_reply)
