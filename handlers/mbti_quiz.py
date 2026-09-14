"""
handlers/mbti_quiz.py - MBTI xarakter testi va natijalarni tahlil qilish moduli.
"""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from aiogram.filters import Command

from data.mbti_data import MBTI_QUESTIONS, MBTI_PROFILES
from handlers.keyboards import get_mbti_keyboard, get_main_keyboard

router = Router()

class MBTIState(StatesGroup):
    answering = State()

@router.message(Command("mbti"))
@router.message(F.text == "🧠 Xarakter testi (MBTI)")
@router.callback_query(F.data == "nav_mbti")
async def start_mbti_test(event: Message | CallbackQuery, state: FSMContext):
    await state.clear()
    intro_text = (
        "🧠 **MBTI Xarakter Testiga Xush Kelibsiz!**\n\n"
        "Ushbu test sizning shaxsiyatingiz, fikrlash uslubingiz va xarakteringizni (masalan: **ENTP, INTJ, INFP...**) "
        "aniqlab, kuchli tomonlaringizni tushunishga yordam beradi.\n\n"
        "📋 Test **8 ta qisqa hayotiy savoldan** iborat.\n"
        "Har bir savolga o'zingizga eng yaqin bo'lgan variantni tanlang.\n\n"
        "Tayyor bo'lsangiz, birinchi savol:"
    )
    if isinstance(event, CallbackQuery):
        await event.answer()
        await event.message.answer(intro_text, parse_mode="Markdown")
        await send_mbti_question(event.message, question_idx=0, state=state)
    else:
        await event.answer(intro_text, parse_mode="Markdown")
        await send_mbti_question(event, question_idx=0, state=state)

async def send_mbti_question(message_or_query, question_idx: int, state: FSMContext):
    q = MBTI_QUESTIONS[question_idx]
    text = (
        f"📊 **Savol {question_idx + 1} / {len(MBTI_QUESTIONS)}:**\n\n"
        f"❓ **{q['question']}**\n\n"
        f"🅰️ {q['option_a'][0]}\n\n"
        f"🅱️ {q['option_b'][0]}"
    )
    kb = get_mbti_keyboard(question_idx)
    
    await state.update_data(current_idx=question_idx)
    await state.set_state(MBTIState.answering)

    if isinstance(message_or_query, Message):
        await message_or_query.answer(text, reply_markup=kb, parse_mode="Markdown")
    else:
        await message_or_query.message.edit_text(text, reply_markup=kb, parse_mode="Markdown")

@router.callback_query(F.data.startswith("mbti_"))
async def handle_mbti_answer(call: CallbackQuery, state: FSMContext):
    data = call.data
    
    if data == "mbti_cancel":
        await state.clear()
        await call.message.edit_text("❌ **Test bekor qilindi.** Istalgan vaqtda qayta boshlashingiz mumkin.")
        await call.answer("Test bekor qilindi.")
        return

    # mbti_{idx}_{choice}
    parts = data.split("_")
    idx = int(parts[1])
    choice = parts[2] # 'A' yoki 'B'

    q = MBTI_QUESTIONS[idx]
    selected_letter = q['option_a'][1] if choice == 'A' else q['option_b'][1]

    # Javoblarni yangilash
    user_data = await state.get_data()
    answers = user_data.get("answers", [])
    answers.append(selected_letter)
    await state.update_data(answers=answers)
    await call.answer()

    next_idx = idx + 1
    if next_idx < len(MBTI_QUESTIONS):
        await send_mbti_question(call, question_idx=next_idx, state=state)
    else:
        # Natijani hisoblash
        await calculate_and_send_mbti_result(call, answers, state)

async def calculate_and_send_mbti_result(call: CallbackQuery, answers: list, state: FSMContext):
    # 4 o'q bo'yicha hisoblash
    # E vs I
    e_count = answers.count("E")
    i_count = answers.count("I")
    dim1 = "E" if e_count >= i_count else "I"

    # S vs N
    s_count = answers.count("S")
    n_count = answers.count("N")
    dim2 = "S" if s_count >= n_count else "N"

    # T vs F
    t_count = answers.count("T")
    f_count = answers.count("F")
    dim3 = "T" if t_count >= f_count else "F"

    # J vs P
    j_count = answers.count("J")
    p_count = answers.count("P")
    dim4 = "J" if j_count >= p_count else "P"

    mbti_type = f"{dim1}{dim2}{dim3}{dim4}"
    profile = MBTI_PROFILES.get(mbti_type, MBTI_PROFILES["INTJ"])

    strengths_str = "\n".join([f"• {s}" for s in profile["strengths"]])
    weaknesses_str = "\n".join([f"• {w}" for w in profile["weaknesses"]])
    careers_str = "\n".join([f"💼 {c}" for c in profile["careers"]])

    result_text = (
        f"🎉 **TEST YAKUNLANDI! SIZNING NATIJANGIZ:**\n\n"
        f"👑 **{profile['title']}**\n\n"
        f"📖 **Xarakteringiz haqida:**\n{profile['desc']}\n\n"
        f"💪 **Kuchli tomonlaringiz:**\n{strengths_str}\n\n"
        f"⚠️ **E'tibor berish kerak bo'lgan nozik jihatlar:**\n{weaknesses_str}\n\n"
        f"🎯 **Sizga eng mos keluvchi kasbiy sohalar:**\n{careers_str}\n\n"
        f"💡 **Ustozona maslahat:**\n_{profile['advice']}_\n\n"
        f"*(Keyingi qadam: '💼 Kasb tanlash testi' orqali o'zingizga mos aniq zamonaviy kasblarni ham bilib olishingiz mumkin!)*"
    )

    await state.clear()
    await call.message.edit_text(result_text, parse_mode="Markdown")
    await call.message.answer(
        "Bosh menyudan boshqa bo'limlarni ham tanlashingiz mumkin: 👇",
        reply_markup=get_main_keyboard()
    )
