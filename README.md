# 🌟 Psixolog, Qaror Qabul Qilish Ustozi va G'oyalar Boti (Telegram Bot)

Ushbu loyiha Python dasturlash tili, **aiogram 3** asinxron freymvorki va **Google Gemini AI** asosida yaratilgan aqlli Telegram botidir.

---

## 🎯 Botning Maqsadi va Funksiyalari

1. **🧠 Psixolog va Yordamchi Maslahatchi:**
   - Foydalanuvchini faol tinglaydi, hissiyotlarini tushunadi va ruhiy dalda beradi.
   - Stress, xavotir va tushkunlikda xotirjamlikka chorlaydi.
   
2. **🤝 Muammo va Vaziyatlarni Chuqur Tahlil Qilish:**
   - Oddiy yoki murakkab aytilgan har qanday ahvolni tushunadi. Agar muammo juda umumiy bo'lsa, **vaziyatni to'liqroq va batafsilroq izohlab berishini so'raydi**.
   - Vaziyat tushuntirilgach, uning asl tub sabablari va ildizlarini ochib beradi.

3. **🔮 Ehtimoliy Ssenariylar va Oqibatlar Prognozi (/tahlil):**
   - Vaziyatdan kelib chiquvchi kelajakdagi ehtimoliy xavflar, harakatsizlik oqibati va ijobiy imkoniyatlarni prognoz qiladi.

4. **🛠️ Ko'p Variantli Yechimlar (Variant A, B, C):**
   - Muammoga birgina yo'l emas, balki bir nechta yechim variantlarini taqdim etadi:
     * **Variant 1:** Tezkor va xavfsiz qadamlar.
     * **Variant 2:** Tizimli va strategik uzoq muddatli yechim.
     * **Variant 3:** Kreativ va nostandart yondashuv.

5. **📜 Chuqur Falsafiy va Hayotiy Mushohada (/falsafa):**
   - Hayot mazmuni, borliq, qadriyatlar, inson erkinligi va ruhiy dunyosi bo'yicha Sharq (Rumiy, Navoiy, Forobiy, Ibn Sino) va jahon tafakkuri uyg'unligida mazmunli mulohazalar yuritadi.

6. **🧭 Qaror Qabul Qilishda Ustoz (/qaror):**
   - Variantlarning plyus va minuslarini tahlil qiladi (10-10-10 qoidasi, SWOT tahlili).

8. **🧠 Xarakter Testi (MBTI — ENTP, INTJ, INFP...):**
   - 8 ta qiziqarli hayotiy savol asosida foydalanuvchining 16 ta MBTI tipidan qaysi biriga mansubligini aniqlaydi.
   - Xarakterning kuchli va nozik jihatlari, munosabatlar uslubi va ustozona tavsiyalarni beradi.

9. **💼 Kasb Tanlash Testi (Karyera Orientatsiyasi):**
   - Qobiliyat va qiziqishlarga qarab, foydalanuvchiga mos keluvchi **alohida aniq zamonaviy kasblar ro'yxatini (Top 4)**, ularning talablari va o'rganish yo'l xaritasini (roadmap) taqdim etadi.

10. **🌱 Shaxsiy Rivojlanish va Kamolot:**
    - Atom odatlar shakllantirish, vaqtni boshqarish (Pomodoro, Eisenxauer), eng sara kitoblar ro'yxati va ruhiy xotirjamlik mashqlarini o'rgatadi.
    - AI orqali individual maqsadlar bo'yicha maxsus reja tuzib beradi.

---

## 🛡️ Qat'iy Xavfsizlik va Maxsus Yo'naltirish Qoidalari

* **🌿 Sog'liq va Tibbiyot masalalari:**
  - Bot hech qachon dori tavsiya qilmaydi yoki tashxis qo'ymaydi.
  - Avval oddiy, zararsiz va tabiiy qisqa tavsiya beradi (bir stakan toza suv ichish, toza havoda sayr qilish, yengil dush qabul qilish, chuqur nafas olib dam olish).
  - So'ngra albatta **"Ushbu mavzu doirasida malakali shifokor yoki tibbiyot xodimlari bilan maslahatlashish zarur"** deb mutaxassisga yo'naltiradi.

* **⚖️ Siyosiy masalalar:**
  - Hech qanday subyektiv, tarafkash yoki his-tuyg'ularga berilgan fikr bildirmaydi.
  - Faqat rasmiy va ishonchli manbalarga tayanib, **to'liq neytral (xolis)** va muvozanatli ma'lumot beradi.

* **🌙 Din masalalari:**
  - Kundalik odob-axloq, insoniylik va munosabatlarda **O'zbek xalqining milliy va an'anaviy qadriyatlariga** asoslanib samimiy javob beradi.
  - Chuqur diniy doiradagi masalalarda (fatvo, shariat hukmlari, aqida yoki fiqhiy tortishuvlar) **diniy ulamolar yoki O'zbekiston Musulmonlari idorasi (muslim.uz / fatvo.uz)** kabi rasmiy idoralarga murojaat qilishni qat'iy tavsiya qiladi.

---

## 📁 Loyiha Fayllari Tuzilmasi

```text
new n27/
├── bot.py              # Asosiy kirish fayli (botni ishga tushirish)
├── config.py           # Konfiguratsiya va .env faylini yuklovchi modul
├── guardrails.py       # Sog'liq, din, vaziyatni so'rash kabi xavfsizlik filtrlari
├── ai_service.py       # Google Gemini AI integratsiyasi va System Prompt
├── test_bot.py         # Qoidalar va filtrlarni sinovdan o'tkazuvchi test skripti
├── handlers/
│   ├── __init__.py
│   ├── commands.py     # /start, /help, /yangi, /qaror, /goya buyruqlari
│   └── chat.py         # Foydalanuvchi matnlarini qabul qilish va AI bilan bog'lash
├── .env.example        # Tokenlar va kalitlar uchun namuna
├── .env                # Sizning maxfiy tokenlaringiz saqlanadigan fayl
└── requirements.txt    # Kerakli Python kutubxonalari
```

---

## 🚀 O'rnatish va Ishga Tushirish

### 1. Python virtual muhitini yaratish va faollashtirish
Loyihaning asosiy papkasida terminalni oching va quyidagilarni bajaring:

```bash
# Virtual muhit yaratish
python -m venv venv

# Windows tizimida faollashtirish:
.\venv\Scripts\activate

# Linux yoki macOS tizimida faollashtirish:
# source venv/bin/activate
```

### 2. Kutubxonalarni o'rnatish
```bash
pip install -r requirements.txt
```

### 3. Telegram Bot Token va Gemini API kalitini olish

1. **Telegram Bot Token:**
   - Telegramda [@BotFather](https://t.me/BotFather) botini oching.
   - `/newbot` buyrug'ini bering, b соцingizga nom va username tanlang.
   - BotFather sizga bergan tokenni nusxalab oling.

2. **Google Gemini API Kaliti (Bepul):**
   - [Google AI Studio](https://aistudio.google.com/) saytiga kiring (Google hisobingiz bilan).
   - "Get API key" tugmasini bosib, yangi API kalit yarating va nusxalab oling.

### 4. `.env` faylini to'ldirish
Loyiha ichidagi `.env` faylini istalgan matn muharriri (yoki Notepad) bilan oching va o'z ma'lumotlaringizni yozing:

```env
BOT_TOKEN=1234567890:AAH...sizning_telegram_bot_tokeningiz
GEMINI_API_KEY=AIzaSy...sizning_gemini_api_kalitingiz
GEMINI_MODEL=gemini-1.5-flash
```

### 5. Sinov testini yurgazish
Qoidalar va filtrlarning to'g'ri ishlashini tekshirish uchun:
```bash
python test_bot.py
```

### 6. Botni ishga tushirish! 🎉
```bash
python bot.py
```

Endi Telegramda o'z botingizga kiring va `/start` buyrug'ini yuboring!

---

## 💬 Mavjud Buyruqlar

- `/start` - Bot bilan tanishuv, imkoniyatlar va qoidalar.
- `/tahlil` - Vaziyatni chuqur tahlil qilish, ehtimoliy ssenariylar prognozi va variantlar olish.
- `/falsafa` - Falsafiy va hayotiy mushohada, Sharq va jahon donishmandligi.
- `/qaror` - Ikkilanayotgan masalada to'g'ri qaror qabul qilish tizimi.
- `/goya` - Yangi g'oyalar va nostandart yechimlar generatori.
- `/yangi` - Oldingi suhbat tarixini tozalab, yangi mavzu boshlash.
- `/help` - Yordam va botdan samarali foydalanish bo'yicha maslahatlar.
