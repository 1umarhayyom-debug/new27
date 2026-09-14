"""
ai_service.py - Sun'iy intellekt integratsiyasi (OpenAI GPT va Google Gemini AI).
Foydalanuvchi bilan muloqot, psixologik qo'llab-quvvatlash, qaror qabul qilish va chuqur tahlil.
"""

import logging
from typing import Dict, List

from config import OPENAI_API_KEY, OPENAI_MODEL, GEMINI_API_KEY, GEMINI_MODEL

try:
    from openai import AsyncOpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    AsyncOpenAI = None
    OPENAI_AVAILABLE = False

try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError:
    genai = None
    GENAI_AVAILABLE = False

logger = logging.getLogger(__name__)

# Tizimli ko'rsatma (System Instruction)
SYSTEM_PROMPT = """
Siz — oqil, samimiy, falsafiy mushohadaga ega dono psixolog, hayotiy ustoz (mentor), 
qaror qabul qilishda strategik yo'lboshchi va har qanday murakkab vaziyatga chuqur tahlil hamda ko'p variantli yechim beruvchi sun'iy intellektsiz.

SIZNING ASOSIY VAZIFALARINGIZ VA XULQ-ATVORINGIZ:

1. CHUQUR FALSAFIY VA HAYOTIY MUSOHADA:
- Agar foydalanuvchi chuqur falsafiy qarashlar, hayot mazmuni, borliq, qadriyatlar, inson taqdiri, erkinlik yoki ruhiy holat haqida yozsa:
  Sharqona va jahon donishmandligi (Alisher Navoiy, Jaloliddin Rumiy, Abu Ali ibn Sino va zamonaviy falsafiy-psixologik qarashlar) uyg'unligida teran, mazmunli va mulohazakor javob bering.
- Falsafani shunchaki quruq nazariya emas, balki insonning amaliy hayotiga tinchlik, saboq va yorug'lik olib kiruvchi mayoq sifatida tushuntiring.

2. ODDIY YOKI MURAKKAB AHVOL VA VAZIYATLARNI CHUQUR TAHLIL QILISH:
- Foydalanuvchi o'z ahvolini xoh oddiy xalqona tilda, xoh murakkab izohlasin — uni diqqat bilan tinglang.
- Vaziyatning tub ildizlarini ochib bering: "Bu holat aslida nima sababdan yuzaga kelgan bo'lishi mumkin?" degan savolga tahliliy javob toping.
- Agar muammo juda qisqa yoki mujmal bo'lsa, avval vaziyatni to'liqroq izohlab berishini so'rang. Vaziyat tushuntirilgach esa chuqur tahlilga o'ting.

3. EHTIMOLIY KELIB CHIQUVCHI VAZIYATLAR VA OQIBATLARNI PROGNOZ QILISH (SCENARIO ANALYSIS):
Har qanday muhim vaziyat yoki muammoni tahlil qilganda, kelajakda nimalar sodir bo'lishi mumkinligini ko'rsating:
- Agar hech narsa o'zgartirilmasa (harakatsizlik oqibati): Vaziyat qanday yomonlashishi yoki qanday yangi muammolarni keltirib chiqarishi mumkin?
- Ehtimoliy xavflar va kutilmagan to'siqlar: Foydalanuvchi qaysi nozik jihatlarni e'tibordan chetda qoldirayotgan bo'lishi mumkin?
- Ijobiy imkoniyatlar: Bu vaziyatdan qanday ijobiy tajriba va o'sish sabog'ini olish mumkin?

4. KO'P VARIANTLI YECHIMLAR VA AMALIY TAKLIFLAR TAQDIM ETISH:
Foydalanuvchiga faqat bitta yo'lni majburlamang. Har doim bir nechta puxta o'ylangan variantlarni taklif qiling:
- Variant 1 (Tezkor va xavfsiz qadam): Hozirning o'zida keskinlikni pasaytirish va vaziyatni barqarorlashtirish yo'li.
- Variant 2 (Tizimli va uzoq muddatli yechim): Muammoning ildizini yo'qotuvchi, sabr va reja talab qiladigan asosiy yo'l.
- Variant 3 (Kreativ / Nostandart yondashuv): Masalaga yangicha qarash, kutilmagan imkoniyatdan foydalanish.
Har bir variantning o'ziga xos plyus va minuslarini ko'rsatib bering.

5. QAROR QABUL QILISHDA USTOZLIK:
- Tanlovlar orasida ikkilanayotganda 10-10-10 qoidasi (10 daqiqa, 10 oy, 10 yildan keyingi ta'siri), SWOT tahlili va ehtimoliy risklarni boshqarishga o'rgating.
- Yakuniy xulosa va tanlovni foydalanuvchining o'ziga qoldiring, lekin unga mustahkam asos bering.

6. SOG'LIQ MASALALARIDAGI QAT'IY QOIDA:
- Har qanday jismoniy salomatlik, kasallik, dori yoki alomat so'ralganda:
  a) Avval oddiy, zararsiz va tabiiy qisqa tavsiya bering (bir stakan toza iliq suv ichish, toza havoda sayr qilish, yengil dush qabul qilish, chuqur nafas olib dam olish).
  b) So'ngra qat'iy ravishda: "Ushbu mavzu doirasida malakali shifokor yoki tibbiyot xodimlari bilan maslahatlashish zarur" deb uqtiring. Hech qachon dori tavsiya qilmang yoki tibbiy tashxis qo'ymang!

7. SIYOSIY MASALALARDAGI QAT'IY QOIDA:
- Hech qanday subyektiv, emotsional yoki tarafkash fikr bildirmang.
- Faqat tegishli, rasmiy va xalqaro tan olingan xolis manbalar nuqtai nazaridan to'liq NEYTRAL (xolis) va muvozanatli ma'lumot bering.

8. DIN MASALALARIDAGI QAT'IY QOIDA:
- Kundalik odob-axloq, insoniy munosabatlar va qadriyatlar masalasida: O'ZBEK XALQINING MILLIY VA AN'ANAVIY QADRIYATLARIGA, o'zaro hurmat, sabr va odob madaniyatiga asosan samimiy javob bering.
- Agar savol chuqur diniy doiradagi masala, shariat hukmi, fiqhiy tortishuv yoki fatvo haqida bo'lsa: "Bu masala yuzasidan diniy ulamolar yoki O'zbekiston Musulmonlari idorasi (muslim.uz / fatvo.uz) kabi rasmiy idoralarga murojaat qilish zarur" deb javob bering va o'zingiz hukm chiqarmang.

TIL VA USLUB:
- O'zbek tilining adabiy, chuqur, samimiy va chiroyli uslubida so'zlang.
- Murakkab fikrlarni aniq, qismlarga ajratilgan (tahlil, ehtimoliy oqibatlar, yechim variantlari) holda qulay formatda taqdim eting.
"""

# Foydalanuvchilar suhbat tarixini saqlash
user_chats: Dict[int, any] = {}

# Mijozlar (Clients)
_openai_client = None
_gemini_model = None

def get_openai_client():
    global _openai_client
    if not OPENAI_AVAILABLE or not OPENAI_API_KEY:
        return None
    if _openai_client is None:
        try:
            _openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)
            logger.info(f"OpenAI mijozi muvaffaqiyatli ulandi (Model: {OPENAI_MODEL}).")
        except Exception as e:
            logger.error(f"OpenAI ulanishida xatolik: {e}")
            _openai_client = None
    return _openai_client

def get_gemini_model():
    global _gemini_model
    if not GENAI_AVAILABLE or not GEMINI_API_KEY:
        return None
    if _gemini_model is None:
        try:
            genai.configure(api_key=GEMINI_API_KEY)
            _gemini_model = genai.GenerativeModel(
                model_name=GEMINI_MODEL,
                system_instruction=SYSTEM_PROMPT,
                generation_config={
                    "temperature": 0.7,
                    "top_p": 0.95,
                    "max_output_tokens": 1200,
                }
            )
            logger.info("Gemini AI modeli muvaffaqiyatli ishga tushirildi.")
        except Exception as e:
            logger.error(f"Gemini AI modelini ulashda xatolik: {e}")
            _gemini_model = None
    return _gemini_model

def clear_user_history(user_id: int):
    """Foydalanuvchi suhbat tarixini tozalash (/yangi buyrug'i uchun)"""
    if user_id in user_chats:
        del user_chats[user_id]

async def _call_openai(client: AsyncOpenAI, user_id: int, message_text: str) -> str:
    """OpenAI GPT modeli orqali javob olish"""
    if user_id not in user_chats or not isinstance(user_chats[user_id], list):
        user_chats[user_id] = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
    
    history = user_chats[user_id]
    history.append({"role": "user", "content": message_text})
    
    # Tarix juda uzayib ketmasligi uchun oxirgi 16 ta xabarni saqlash
    if len(history) > 17:
        user_chats[user_id] = [history[0]] + history[-16:]
        history = user_chats[user_id]

    response = await client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=history,
        temperature=0.7,
        max_tokens=1500
    )
    
    reply = response.choices[0].message.content.strip()
    history.append({"role": "assistant", "content": reply})
    return reply

async def _call_gemini(model, user_id: int, message_text: str) -> str:
    """Gemini modeli orqali javob olish"""
    if user_id not in user_chats or isinstance(user_chats[user_id], list):
        user_chats[user_id] = model.start_chat(history=[])
    chat = user_chats[user_id]
    response = await chat.send_message_async(message_text)
    return response.text.strip()

async def generate_response(user_id: int, message_text: str) -> str:
    """Foydalanuvchi xabariga javob yaratish (OpenAI yoki Gemini)"""
    # 1. Avval OpenAI tekshirish
    openai_client = get_openai_client()
    if openai_client:
        try:
            return await _call_openai(openai_client, user_id, message_text)
        except Exception as e:
            logger.error(f"OpenAI xatosi: {e}")

    # 2. Keyin Gemini tekshirish
    gemini_model = get_gemini_model()
    if gemini_model:
        try:
            return await _call_gemini(gemini_model, user_id, message_text)
        except Exception as e:
            logger.error(f"Gemini xatosi: {e}")

    # 3. Agar API kalitlar ishlamasa (Zaxira rejim)
    return (
        "🌱 **Sizning fikringizni diqqat bilan o'qidim va tushundim.**\n\n"
        "Ushbu holatni tizimli tahlil qilish uchun quyidagi 3 ta jihatga e'tibor qaratishni tavsiya etaman:\n\n"
        "1️⃣ **Vaziyat ildizi:** Bu holat nima sababdan yuzaga kelganini aniqlab oling (tashqi omillarmi yoki ichki ikkilanishlarmi?).\n"
        "2️⃣ **Ehtimoliy ssenariy:** Agar hech narsa o'zgartirilmasa, vaziyat 1 oydan so'ng qanday bo'ladi?\n"
        "3️⃣ **Qaror variantlari:**\n"
        "   • **Variant A (Tezkor):** Hozirning o'zida ruhiy xotirjamlikni ta'minlaydigan kichik qadam tashlash.\n"
        "   • **Variant B (Tizimli):** Reja tuzib, har bir to'siqni bosqichma-bosqich yechish.\n"
        "   • **Variant C (Yangi burchak):** Boshqa tajribali insonlardan xolis fikr so'rash.\n\n"
        "*(💡 Jonli AI tahlili faol bo'lishi uchun API kalit to'g'ri kiritilganiga ishonch hosil qiling.)*"
    )
