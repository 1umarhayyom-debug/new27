"""
handlers/keyboards.py - Bot klaviaturalari (ReplyKeyboardMarkup va InlineKeyboardMarkup).
"""

from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

def get_main_keyboard() -> ReplyKeyboardMarkup:
    """Asosiy menyu klaviaturasi (pastdagi doimiy tugmalar)"""
    kb = [
        [
            KeyboardButton(text="🧠 Xarakter testi (MBTI)"),
            KeyboardButton(text="💼 Kasb tanlash testi")
        ],
        [
            KeyboardButton(text="🌱 Shaxsiy rivojlanish"),
            KeyboardButton(text="💬 Psixolog bilan suhbat")
        ],
        [
            KeyboardButton(text="🔄 Bosh menyu")
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, is_persistent=True)

def get_main_inline_keyboard() -> InlineKeyboardMarkup:
    """Xabar ichidagi to'g'ridan-to'g'ri ko'rinuvchi interaktiv tugmalar"""
    kb = [
        [
            InlineKeyboardButton(text="🧠 Xarakter testi (MBTI)", callback_data="nav_mbti"),
            InlineKeyboardButton(text="💼 Kasb tanlash testi", callback_data="nav_career")
        ],
        [
            InlineKeyboardButton(text="🌱 Shaxsiy rivojlanish", callback_data="nav_growth"),
            InlineKeyboardButton(text="💬 Psixolog bilan suhbat", callback_data="nav_chat")
        ],
        [
            InlineKeyboardButton(text="🔍 Vaziyat tahlili (/tahlil)", callback_data="nav_tahlil"),
            InlineKeyboardButton(text="📜 Falsafiy mushohada (/falsafa)", callback_data="nav_falsafa")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)

def get_mbti_keyboard(question_id: int) -> InlineKeyboardMarkup:
    """MBTI savoli uchun 2 ta tanlov tugmasi"""
    kb = [
        [InlineKeyboardButton(text="🅰️ 1-variant", callback_data=f"mbti_{question_id}_A")],
        [InlineKeyboardButton(text="🅱️ 2-variant", callback_data=f"mbti_{question_id}_B")],
        [InlineKeyboardButton(text="❌ Testni bekor qilish", callback_data="mbti_cancel")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)

def get_career_keyboard(question_id: int) -> InlineKeyboardMarkup:
    """Kasb tanlash savoli uchun 4 ta tanlov tugmasi"""
    kb = [
        [InlineKeyboardButton(text="1️⃣ Variant A", callback_data=f"career_{question_id}_0")],
        [InlineKeyboardButton(text="2️⃣ Variant B", callback_data=f"career_{question_id}_1")],
        [InlineKeyboardButton(text="3️⃣ Variant C", callback_data=f"career_{question_id}_2")],
        [InlineKeyboardButton(text="4️⃣ Variant D", callback_data=f"career_{question_id}_3")],
        [InlineKeyboardButton(text="❌ Testni bekor qilish", callback_data="career_cancel")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)

def get_growth_keyboard() -> InlineKeyboardMarkup:
    """Shaxsiy rivojlanish bo'limi interaktiv tugmalari"""
    kb = [
        [
            InlineKeyboardButton(text="🎯 Atom odatlar", callback_data="growth_habits"),
            InlineKeyboardButton(text="⏳ Vaqt boshqaruvi", callback_data="growth_time")
        ],
        [
            InlineKeyboardButton(text="📚 Kitoblar tavsiyasi", callback_data="growth_books"),
            InlineKeyboardButton(text="🧘 Stress va xotirjamlik", callback_data="growth_calm")
        ],
        [
            InlineKeyboardButton(text="💡 AI dan individual maslahat", callback_data="growth_ai_advice")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)
