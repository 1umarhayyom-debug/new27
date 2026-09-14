"""
handlers/growth.py - Shaxsiy rivojlanish, odatlar, vaqt boshqaruvi va tavsiyalar moduli.
"""

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from handlers.keyboards import get_growth_keyboard

router = Router()

@router.message(Command("rivojlanish"))
@router.message(F.text == "🌱 Shaxsiy rivojlanish")
@router.callback_query(F.data == "nav_growth")
async def cmd_growth(event: Message | CallbackQuery):
    text = (
        "🌱 **Shaxsiy Rivojlanish va Kamolot Bo'limi:**\n\n"
        "Har bir inson har kuni o'zining kechagi holatidan 1% bo'lsa-da yaxshiroq bo'lishi mumkin. "
        "Ushbu bo'limda siz hayotingizni tartibga solish, intizomni mustahkamlash va salohiyatingizni "
        "to'liq ochish uchun amaliy tavsiyalarni topasiz.\n\n"
        "Qaysi yo'nalish bo'yicha maslahat olmoqchisiz? Quyidagi tugmalardan birini tanlang: 👇"
    )
    if isinstance(event, CallbackQuery):
        await event.answer()
        await event.message.answer(text, reply_markup=get_growth_keyboard(), parse_mode="Markdown")
    else:
        await event.answer(text, reply_markup=get_growth_keyboard(), parse_mode="Markdown")

@router.callback_query(F.data == "growth_habits")
async def growth_habits(call: CallbackQuery):
    text = (
        "🎯 **Atom Odatlar (Odatlarni Shakllantirish San'ati):**\n\n"
        "Katta natijalar — kichik odatlarning kundalik takrorlanishidan paydo bo'ladi.\n\n"
        "1. **2 Daqiqa Qoidasi:** Yangi odatni boshlashda uni dastlab 2 daqiqadan ko'p vaqt olmaydigan qiling "
        "(masalan: 1 sahifa kitob o'qish, 5 marta mashq qilish).\n"
        "2. **Odatlarni zanjirlash:** Yangi odatni allaqachon mavjud odatingizga bog'lang. "
        "*(Misol: 'Ertalab qahva ichgach [eski odat], 5 daqiqa kunlik reja yozaman [yangi odat]').*\n"
        "3. **Muhitni to'g'rilash:** Yaxshi odatlarni boshlashni imkon qadar osonlashtiring, "
        "zararlilarini esa qiyinlashtiring (masalan: telefonni ish paytida boshqa xonaga qo'yish).\n"
        "4. **Hech qachon 2 kun ketma-ket qoldirmang:** Bir kun o'xshamasa ham, keyingi kuni albatta davom ettiring!"
    )
    await call.message.answer(text, parse_mode="Markdown")
    await call.answer()

@router.callback_query(F.data == "growth_time")
async def growth_time(call: CallbackQuery):
    text = (
        "⏳ **Vaqtni Boshqarish va Yuqori Unumdorlik (Time Management):**\n\n"
        "Vaqt — ortga qaytmaydigan eng qimmatbaho resursingizdir.\n\n"
        "• 🍅 **Pomodoro Texnikasi:** 25 daqiqa chalg'imasdan diqqat bilan ishlang, keyin 5 daqiqa dam oling. "
        "Har 4 ta oraliqdan so'ng 20-30 daqiqa katta tanaffus qiling.\n"
        "• 📊 **Eisenxauer Matritsasi:** Har tong vazifalarni 4 guruhga ajrating:\n"
        "  1. *Muhim va Shoshilinch* — darhol bajaring;\n"
        "  2. *Muhim, lekin Shoshilinch emas* — eng ko'p e'tibor qaratilishi kerak bo'lgan soha (strategik o'sish);\n"
        "  3. *Shoshilinch, lekin Muhim emas* — birovga topshiring;\n"
        "  4. *Muhim ham emas, Shoshilinch ham emas* — hayotingizdan butunlay chiqarib tashlang.\n"
        "• 🐸 **'Qurbaqani yeng':** Kuningizdagi eng og'ir, eng yoqimsiz, ammo eng muhim vazifani ertalab birinchi navbatda bajaring."
    )
    await call.message.answer(text, parse_mode="Markdown")
    await call.answer()

@router.callback_query(F.data == "growth_books")
async def growth_books(call: CallbackQuery):
    text = (
        "📚 **Shaxsiy Rivojlanish Uchun O'qilishi Shart Bo'lgan Top Kitoblar:**\n\n"
        "1. 📖 **'Atom Odatlar' (Jeyms Klir)** — kichik odatlar orqali hayotni butunlay o'zgartirish bo'yicha jahon bestselleri.\n"
        "2. 📖 **'Muvaffaqiyatli insonlarning 7 ko'nikmasi' (Stiven Kovi)** — xarakter, tamoyillar va samaradorlik poydevori.\n"
        "3. 📖 **'Hayotga 'Ha' demoq' (Viktor Frankl)** — inson har qanday qiyinchilikda qanday qilib hayot mazmunini topishi mumkinligi haqida ruhiy durdona.\n"
        "4. 📖 **'Chuqur ish' (Kal Nyuport)** — chalg'ituvchi dunyoda diqqatni jamlash va yuqori natijalarga erishish qo'llanmasi.\n"
        "5. 📖 **'O'yla va boy bo'l' (Napoleon Xill)** — to'g'ri fikrlash va maqsad sari sabot bilan yurish falsafasi."
    )
    await call.message.answer(text, parse_mode="Markdown")
    await call.answer()

@router.callback_query(F.data == "growth_calm")
async def growth_calm(call: CallbackQuery):
    text = (
        "🧘 **Ruhiy Xotirjamlik va Ichki Muvozanat:**\n\n"
        "Tinch qalb — har qanday muvaffaqiyat va baxtning kalitidir.\n\n"
        "• 🌬 **4-7-8 Nafas Mashqi:** 4 soniya davomida burningizdan chuqur nafas oling, "
        "7 soniya nafasingizni ushlab turing, 8 soniya davomida og'zingizdan sekin chiqaring. "
        "Bu asab tizimini darhol tinchlantiradi.\n"
        "• 📝 **Shukronalik kundaligi:** Har oqshom yotishdan oldin bugun hayotingizda sodir bo'lgan "
        "3 ta kichik yaxshilik uchun shukr qiling va ularni yozib qo'ying.\n"
        "• 📵 **Raqamli detoks:** Kuniga kamida 1 soat (ayniqsa uyg'onganda va uxlashdan oldin) "
        "telefonsiz va ekransiz vaqt o'tkazing.\n"
        "• 🚶‍♂️ **Tabiat bilan muloqot:** Har kuni kamida 15-20 daqiqa toza havoda shoshilmasdan sayr qiling."
    )
    await call.message.answer(text, parse_mode="Markdown")
    await call.answer()

@router.callback_query(F.data == "growth_ai_advice")
async def growth_ai_advice(call: CallbackQuery):
    text = (
        "💡 **AI dan Shaxsiy Rivojlanish Bo'yicha Individual Maslahat:**\n\n"
        "O'zingiz rivojlantirmoqchi bo'lgan maqsad yoki engib o'tmoqchi bo'lgan zaifligingiz haqida menga yozing "
        "*(masalan: 'Vaqtimni ijtimoiy tarmoqlarda behuda sarflab qo'yyapman, qanday to'xtatsam bo'ladi?' "
        "yoki 'Ertalab barvaqt uyg'onish odatini qanday shakllantirsam bo'ladi?')*.\n\n"
        "Men sizga maxsus individual reja va psixologik tavsiyalar tuzib beraman! ✍️"
    )
    await call.message.answer(text, parse_mode="Markdown")
    await call.answer()
