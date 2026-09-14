"""
guardrails.py - Maxsus mavzular bo'yicha qoidalar va xavfsizlik filtri.
Foydalanuvchi talablariga asosan:
1. Sog'liq masalalari: kichik tabiiy tavsiya (toza havo, suv, dush, dam olish) + shifokorga yo'naltirish.
2. Chuqur diniy masalalar: O'zbek xalqi qadriyatlari hurmati + rasmiy diniy idora/ulamolarga yo'naltirish.
3. Muammo haqida umumiy/qisqa yozilsa: vaziyatni to'liqroq izohlashni so'rash.
"""

import re
from typing import Optional, Dict

# 1. Tibbiyot va sog'liq bo'yicha kalit so'zlar
HEALTH_KEYWORDS = [
    r"\bdori\b", r"\btabletka\b", r"\bukol\b", r"\bshifoxona\b", r"\bkasal\b", 
    r"\bog'riq\b", r"\bog'riyapti\b", r"\bko'ngil aynishi\b", r"\bistima\b", r"\btemperatura\b",
    r"\bboshim og'riyapti\b", r"\byuragim\b", r"\boshib ketdi\b", r"\bbosim\b", r"\bdavolash\b",
    r"\btashxis\b", r"\bdoza\b", r"\bantibiotik\b", r"\bshamollash\b", r"\bkasallik\b",
    r"\bjarohat\b", r"\boshqozon\b", r"\bko'z og'rig'i\b", r"\brentgen\b", r"\banaliz\b"
]

# 2. Chuqur diniy / fatvo / shariat hukmlari bo'yicha kalit so'zlar
DEEP_RELIGION_KEYWORDS = [
    r"\bfatvo\b", r"\bshariat hukmi\b", r"\bhukm qanday\b", r"\btaloq\b", 
    r"\bnikoh bekor\b", r"\bharommi\b", r"\bhalolmi\b", r"\bkafforat\b",
    r"\bmeros taqsimoti\b", r"\bmazhabiy ixtilof\b", r"\baqida masalasi\b", 
    r"\bnimaga harom\b", r"\bdinda ruxsat bormi\b", r"\bgunohi kabira\b"
]

# 3. Umumiy / noaniq muammo bildirishlari (vaziyatni to'liq so'rash uchun)
VAGUE_PROBLEM_PATTERNS = [
    r"^muammo(m)? bor(\s*)$",
    r"^qiynal(ib ketdim|yapti|yapman)(\s*)$",
    r"^yordam bering(\s*)$",
    r"^maslahat kerak(\s*)$",
    r"^yomon ahvoldaman(\s*)$",
    r"^nima qilishni bilmayapman(\s*)$",
    r"^boshim qotdi(\s*)$",
    r"^tushkunlikdaman(\s*)$",
    r"^hech narsa o'xshamayapti(\s*)$",
    r"^siqilyapman(\s*)$"
]

HEALTH_RESPONSE = (
    "🌿 **Sog'lig'ingiz haqida qayg'urganingiz yaxshi.**\n\n"
    "Har qanday bezovtalikda, avvalo:\n"
    "• Bir stakan toza iliq suv iching;\n"
    "• Toza havoga chiqib, 5-10 daqiqa yengil nafas oling yoki biroz sayr qiling;\n"
    "• Iloji bo'lsa, iliq dush qabul qilib, tinch joyda biroz ko'zlaringizni yumib dam oling.\n\n"
    "⚠️ **Muhim eslatma:** Ushbu mavzu doirasida **malakali shifokor yoki tibbiyot xodimi** bilan maslahatlashish zarur! "
    "Men sun'iy intellekt bo'lganim sababli dori tavsiya qila olmayman yoki tibbiy tashxis qo'ya olmayman. "
    "Iltimos, o'zingizni ehtiyot qiling va mutaxassis ko'rigidan o'ting."
)

DEEP_RELIGION_RESPONSE = (
    "🌙 **Xushmuomalalik va milliy qadriyatlarimiz doirasida:**\n\n"
    "O'zbek xalqining ma'naviy merosi va milliy qadriyatlarida har doim bag'rikenglik, "
    "kattalarga hurmat, yaxshilik va sabr-qanoat ulug'lanadi.\n\n"
    "⚠️ **Shariat va diniy hukmlar bo'yicha:**\n"
    "Bunday chuqur diniy masalalar, fatvolar va shariat hukmlari bo'yicha aniq xulosa chiqarish faqat vakolatli mutaxassislar vakolatiga kiradi. "
    "Shuning uchun bu masala yuzasidan **diniy ulamolar yoki O'zbekiston Musulmonlari idorasi (muslim.uz / fatvo.uz)** kabi "
    "rasmiy diniy idoralarga murojaat qilishingizni tavsiya etaman."
)

CLARIFY_PROBLEM_RESPONSE = (
    "Assalomu alaykum. Sizni eshitishga va tushunishga tayyorman. 🤝\n\n"
    "Sizga eng to'g'ri maslahat, amaliy yechim yoki ruhiy dalda bera olishim uchun, "
    "iltimos, **vaziyatni to'liqroq va batafsilroq izohlab bera olasizmi?**\n\n"
    "Misol uchun:\n"
    "1. Bu holat aynan nima sababdan boshlandi?\n"
    "2. Hozirgi vaziyat sizga yoki rejalaringizga qanday ta'sir qilyapti?\n"
    "3. Siz qaysi yechim yoki yo'nalishlar haqida o'ylayapsiz?\n\n"
    "Batafsil yozsangiz, birgalikda bosqichma-bosqich tahlil qilib, eng maqbul yo'lni topamiz."
)

def check_guardrails(text: str) -> Optional[Dict[str, str]]:
    """
    Xabarni tahlil qiladi va agar maxsus qoidalarga to'g'ri kelsa,
    tayyor javob qaytaradi.
    """
    if not text:
        return None
    
    clean_text = text.strip().lower()
    
    # 1. Qisqa/mavhum muammo yozilgan bo'lsa -> Vaziyatni to'liq so'rash
    for pattern in VAGUE_PROBLEM_PATTERNS:
        if re.search(pattern, clean_text):
            return {
                "type": "clarify_problem",
                "response": CLARIFY_PROBLEM_RESPONSE
            }
            
    # Agar xabar juda qisqa (1-3 so'z) va muammo haqida bo'lsa:
    words = clean_text.split()
    if len(words) <= 3 and any(w in clean_text for w in ["muammo", "yordam", "siqildim", "qiynaldim", "maslahat"]):
        return {
            "type": "clarify_problem",
            "response": CLARIFY_PROBLEM_RESPONSE
        }

    # 2. Sog'liq / tibbiyot masalasi bo'lsa -> Tabiiy tavsiya + shifokorga yo'naltirish
    for pattern in HEALTH_KEYWORDS:
        if re.search(pattern, clean_text):
            return {
                "type": "health",
                "response": HEALTH_RESPONSE
            }

    # 3. Chuqur diniy masala yoki fatvo so'ralsa -> Diniy idora/ulamolarga yo'naltirish
    for pattern in DEEP_RELIGION_KEYWORDS:
        if re.search(pattern, clean_text):
            return {
                "type": "deep_religion",
                "response": DEEP_RELIGION_RESPONSE
            }

    return None
