"""
handlers/commands.py - Botning asosiy buyruqlarini qayta ishlovchi modul (/start, /help, /yangi, /qaror, /goya).
"""

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from ai_service import clear_user_history
from handlers.keyboards import get_main_keyboard, get_main_inline_keyboard

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    user_name = message.from_user.first_name if message.from_user else "do'stim"
    welcome_text = (
        f"Assalomu alaykum, {user_name}! 👋\n\n"
        "Men sizning shaxsiy **psixologik maslahatchingiz, ustozingiz va g'oyalar beruvchi yordamchingizman**.\n\n"
        "Quyidagi bo'limlardan birini tanlang yoki to'g'ridan-to'g'ri o'zingizni qiziqtirgan masalani yozing: 👇"
    )
    # 1. Xabar ichidagi 100% ko'rinuvchi Inline tugmalar
    await message.answer(welcome_text, reply_markup=get_main_inline_keyboard(), parse_mode="Markdown")
    # 2. Pastdagi doimiy panel klaviaturasi
    await message.answer("Tugmalarni pastdagi paneldan ham tanlashingiz mumkin: 👇", reply_markup=get_main_keyboard())

@router.message(Command("menu"))
@router.message(F.text == "🔄 Bosh menyu")
async def show_menu(message: Message):
    await message.answer(
        "📍 **Bosh menyu:** Quyidagi bo'limlardan birini tanlashingiz mumkin: 👇",
        reply_markup=get_main_inline_keyboard(),
        parse_mode="Markdown"
    )

@router.message(F.text == "💬 Psixolog bilan suhbat")
@router.callback_query(F.data == "nav_chat")
async def chat_with_psychologist(event: Message | CallbackQuery):
    text = (
        "💬 **Erkin Suhbat va Psixologik Maslahat Rejimi:**\n\n"
        "O'zingizni qiynayotgan muammo, ikkilanayotgan qaroringiz, ruhiy holatingiz yoki "
        "har qanday hayotiy savolingizni bemalol yozib qoldiring.\n\n"
        "Men sizni tinglashga va birgalikda to'g'ri yechim topishga tayyorman! 😊"
    )
    if isinstance(event, CallbackQuery):
        await event.answer()
        await event.message.answer(text, parse_mode="Markdown")
    else:
        await event.answer(text, parse_mode="Markdown")

@router.callback_query(F.data == "nav_tahlil")
async def callback_tahlil(call: CallbackQuery):
    await call.answer()
    await cmd_tahlil(call.message)

@router.callback_query(F.data == "nav_falsafa")
async def callback_falsafa(call: CallbackQuery):
    await call.answer()
    await cmd_falsafa(call.message)

@router.message(Command("help"))
async def cmd_help(message: Message):
    help_text = (
        "📚 **Mavjud buyruqlar va maslahatlar:**\n\n"
        "/start - Botni qayta ishga tushirish va asosiy tanishuv\n"
        "/tahlil - Vaziyatni chuqur tahlil qilish, ehtimoliy oqibatlar va variantlar olish\n"
        "/falsafa - Chuqur falsafiy va hayotiy mushohada qilish\n"
        "/qaror - Ikkilanayotgan masalada to'g'ri qaror qabul qilish bo'yicha yo'riqnoma\n"
        "/goya - Yangi g'oyalar va yechimlar topish (brainstorming)\n"
        "/yangi - Suhbat tarixini tozalab, yangi mavzu boshlash\n"
        "/help - Ushbu yordam oynasi\n\n"
        "💡 **Maslahat:** Har qanday muammoni yozishda nima sabab bo'lgani, hozirgi vaziyat va maqsadingizni aniq yozsangiz, tahlil va prognoz shunchalik aniq bo'ladi!"
    )
    await message.answer(help_text, parse_mode="Markdown")

@router.message(Command("yangi"))
async def cmd_clear(message: Message):
    clear_user_history(message.from_user.id)
    await message.answer(
        "🧹 **Suhbat tarixi tozalandi!**\n"
        "Yangi mavzu yoki yangi savolingizni bemalol yozishingiz mumkin. Qulog'im sizda! 😊"
    )

@router.message(Command("tahlil"))
async def cmd_tahlil(message: Message):
    text = (
        "🔍 **Chuqur Vaziyat Tahlili va Ehtimoliy Ssenariylar Prognozi:**\n\n"
        "Hayotingizdagi biror murakkab holat, o'zgarish yoki muammoni tahlil qilmoqchi bo'lsangiz, "
        "menga quyidagilarni erkin tilda (oddiy yoki batafsil) yozib yuboring:\n\n"
        "1. **Hozirgi holat:** Nimalar sodir bo'lmoqda?\n"
        "2. **Sabab:** Sizningcha, bu vaziyat nima sababdan yuzaga keldi?\n"
        "3. **Kutayotgan xavfingiz:** Kelajakda nimadan eng ko'p xavotirdasiz?\n\n"
        "Men sizga:\n"
        "• 📌 Vaziyatning asl ildizlarini;\n"
        "• 🔮 Kelajakda kelib chiqishi mumkin bo'lgan ehtimoliy ssenariylarni (xavf va imkoniyatlar);\n"
        "• 🧭 Bosqichma-bosqich bir nechta yechim variantlarini (Variant A, B, C) taqdim etaman!"
    )
    await message.answer(text, parse_mode="Markdown")

@router.message(Command("falsafa"))
async def cmd_falsafa(message: Message):
    text = (
        "📜 **Falsafiy va Hayotiy Mushohada:**\n\n"
        "Borliq, inson umrining mazmuni, ichki ziddiyatlar, taqdir, erkinlik yoki ruhiy ahvolingiz "
        "haqidagi har qanday mulohazalaringizni bemalol yozing.\n\n"
        "Biz birgalikda buyuk mutafakkirlar merosi (Rumiy, Navoiy, Forobiy, Ibn Sino) va jahon tafakkuri "
        "asosida hayotiy saboqlar va ruhiy xotirjamlik topishga harakat qilamiz. Sizni nima o'yga toldirmoqda? 💭"
    )
    await message.answer(text, parse_mode="Markdown")

@router.message(Command("qaror"))
async def cmd_qaror(message: Message):
    text = (
        "🧭 **Qaror qabul qilishda ustozlik (Tizimli tahlil):**\n\n"
        "Biror muhim qaror oldida ikkilanayotgan bo'lsangiz, menga quyidagilarni yozib yuboring:\n\n"
        "1️⃣ **Muammo:** Qaror nima haqida (masalan: ish almashtirish, o'qish, loyiha)?\n"
        "2️⃣ **Variantlar:** Qaysi tanlovlar mavjud (Variant A va Variant B)?\n"
        "3️⃣ **Qo'rquv yoki to'siq:** Sizni eng ko'p nima xavotirga solmoqda?\n\n"
        "Menga shu ma'lumotlarni yozing, biz birgalikda variantlarning ijobiy va salbiy tomonlarini tahlil qilib, 10-10-10 qoidasi bo'yicha to'g'ri yo'lni aniqlaymiz!"
    )
    await message.answer(text, parse_mode="Markdown")

@router.message(Command("goya"))
async def cmd_goya(message: Message):
    text = (
        "💡 **G'oyalar va yechimlar laboratoriyasi:**\n\n"
        "Qaysi sohada yangi g'oyaga ehtiyojingiz bor?\n"
        "• Shaxsiy rivojlanish yoki yangi odatlar shakllantirish\n"
        "• Loyiha, ish yoki tadbirkorlik\n"
        "• Vaqtni boshqarish va unumdorlik\n"
        "• O'qish yoki yangi ko'nikma o'rganish\n\n"
        "O'z maqsadingizni qisqacha yozib qoldiring, men sizga kamida 3-5 ta amaliy va nostandart g'oyani taklif qilaman!"
    )
    await message.answer(text, parse_mode="Markdown")
