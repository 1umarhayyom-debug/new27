"""
handlers/career_quiz.py - Kasb tanlash (Karyera orientatsiyasi) testi va tavsiyalar moduli.
"""

from collections import Counter
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from aiogram.filters import Command
from data.career_data import CAREER_QUESTIONS, CAREER_PROFILES
from handlers.keyboards import get_career_keyboard, get_main_keyboard

router = Router()

class CareerState(StatesGroup):
    answering = State()

@router.message(Command("kasb"))
@router.message(F.text == "💼 Kasb tanlash testi")
@router.callback_query(F.data == "nav_career")
async def start_career_test(event: Message | CallbackQuery, state: FSMContext):
    await state.clear()
    intro_text = (
        "💼 **Kasb Tanlash va Karyera Orientatsiyasi Testiga Xush Kelibsiz!**\n\n"
        "Qaysi kasb sizning qobiliyatingiz, fe'l-atvoringiz va qiziqishingizga eng mos kelishini "
        "aniqlab beramiz.\n\n"
        "📋 Test **5 ta savoldan** iborat.\n"
        "Har bir savolga o'zingizga eng ma'qul kelgan variantni tanlang.\n\n"
        "Boshlashga tayyormisiz? 🚀"
    )
    if isinstance(event, CallbackQuery):
        await event.answer()
        await event.message.answer(intro_text, parse_mode="Markdown")
        await send_career_question(event.message, question_idx=0, state=state)
    else:
        await event.answer(intro_text, parse_mode="Markdown")
        await send_career_question(event, question_idx=0, state=state)

async def send_career_question(message_or_query, question_idx: int, state: FSMContext):
    q = CAREER_QUESTIONS[question_idx]
    
    options_text = ""
    for i, opt in enumerate(q["options"]):
        options_text += f"**{i+1}.** {opt[0]}\n\n"

    text = (
        f"📊 **Savol {question_idx + 1} / {len(CAREER_QUESTIONS)}:**\n\n"
        f"❓ **{q['question']}**\n\n"
        f"{options_text}"
    )
    kb = get_career_keyboard(question_idx)
    
    await state.update_data(current_idx=question_idx)
    await state.set_state(CareerState.answering)

    if isinstance(message_or_query, Message):
        await message_or_query.answer(text, reply_markup=kb, parse_mode="Markdown")
    else:
        await message_or_query.message.edit_text(text, reply_markup=kb, parse_mode="Markdown")

@router.callback_query(F.data.startswith("career_"))
async def handle_career_answer(call: CallbackQuery, state: FSMContext):
    data = call.data
    
    if data == "career_cancel":
        await state.clear()
        await call.message.edit_text("❌ **Kasb tanlash testi bekor qilindi.**")
        await call.answer("Test bekor qilindi.")
        return

    # career_{idx}_{opt_num}
    parts = data.split("_")
    idx = int(parts[1])
    opt_num = int(parts[2])

    q = CAREER_QUESTIONS[idx]
    chosen_category = q["options"][opt_num][1]

    user_data = await state.get_data()
    choices = user_data.get("choices", [])
    choices.append(chosen_category)
    await state.update_data(choices=choices)
    await call.answer()

    next_idx = idx + 1
    if next_idx < len(CAREER_QUESTIONS):
        await send_career_question(call, question_idx=next_idx, state=state)
    else:
        await calculate_and_send_career_result(call, choices, state)

async def calculate_and_send_career_result(call: CallbackQuery, choices: list, state: FSMContext):
    # Eng ko'p tanlangan yo'nalishni topish
    counter = Counter(choices)
    top_track = counter.most_common(1)[0][0]
    
    profile = CAREER_PROFILES.get(top_track, CAREER_PROFILES["tech"])

    careers_blocks = []
    for c in profile["careers"]:
        block = (
            f"📌 **{c['name']}**\n"
            f"• *Faoliyat:* {c['desc']}\n"
            f"• *Nega sizga mos:* {c['why']}\n"
            f"• *Kerakli ko'nikmalar:* `{c['skills']}`"
        )
        careers_blocks.append(block)

    careers_formatted = "\n\n".join(careers_blocks)

    result_text = (
        f"🎯 **SIZNING KARYERA TESTI NATIJANGIZ:**\n\n"
        f"✨ **{profile['title']}**\n\n"
        f"📖 **Umumiy tahlil:**\n{profile['desc']}\n\n"
        f"💼 **Siz uchun tavsiya etiladigan aniq kasblar:**\n\n"
        f"{careers_formatted}\n\n"
        f"🗺 **Qayerdan boshlash kerak (Roadmap):**\n"
        f"_{profile['roadmap']}_"
    )

    await state.clear()
    await call.message.edit_text(result_text, parse_mode="Markdown")
    await call.message.answer(
        "O'zingizni qiziqtirgan boshqa bo'limni tanlashingiz mumkin: 👇",
        reply_markup=get_main_keyboard()
    )
