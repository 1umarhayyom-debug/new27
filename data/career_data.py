"""
data/career_data.py - Kasb tanlash testi (Karyera orientatsiyasi) savollari va kasblar bazasi.
"""

CAREER_QUESTIONS = [
    {
        "id": 1,
        "question": "Sizga qaysi faoliyat turi eng ko'p zavq bag'ishlaydi?",
        "options": [
            ("💻 Kompyuterda kod yozish, raqamlar, tahlil va mantiqiy jumboqlarni yechish", "tech"),
            ("👥 Odamlar bilan muloqot qilish, ularni tinglash, o'rgatish va yordam berish", "people"),
            ("🎨 Rasm chizish, video yaratish, matn yozish va yangi g'oyalar o'ylab topish", "creative"),
            ("📈 Loyihalarni boshqarish, savdo qilish, jamoani yo'naltirish va biznes yuritish", "business")
        ]
    },
    {
        "id": 2,
        "question": "Qanday ish muhitida o'zingizni eng qulay his qilasiz?",
        "options": [
            ("🖥 Tinch xonada yoki masofadan (remote), chuqur diqqat bilan ishlash", "tech"),
            ("🤝 Do'stona jamoa orasida, doimiy suhbatlar va insonlar bilan aloqada", "people"),
            ("✨ Erkin grafik, ijodiy muhit va cheklovlarsiz maydonda", "creative"),
            ("🏢 Tezkor sur'atdagi ofis, muzokaralar va yirik qarorlar qabul qilinadigan davrada", "business")
        ]
    },
    {
        "id": 3,
        "question": "Ishingiz natijasida siz uchun eng muhimi nima?",
        "options": [
            ("⚙️ Murakkab tizimning mukammal va xatosiz ishlashi", "tech"),
            ("❤️ Boshqa bir insonning hayoti yengillashgani va minnatdorligi", "people"),
            ("🌟 Hech kim o'xshatolmagan o'ziga xos go'zallik va asar yaratish", "creative"),
            ("🏆 Katta moliyaviy daromad, jamoa g'alabasi va bozorda yetakchi bo'lish", "business")
        ]
    },
    {
        "id": 4,
        "question": "Qiyin vaziyatga duch kelsangiz, qanday yondashasiz?",
        "options": [
            ("🔍 Barcha ma'lumotlarni yig'ib, sabab-oqibat zanjirini mantiqan tekshiraman", "tech"),
            ("🗣 Yaqinlar va mutaxassislar bilan maslahatlashib, umumiy til topaman", "people"),
            ("💡 Nostandart va kutilmagan kreativ yechim topishga harakat qilaman", "creative"),
            ("⚡️ Xatarlarni hisoblab, zudlik bilan aniq harakatlar rejasini tuzaman", "business")
        ]
    },
    {
        "id": 5,
        "question": "Bo'sh vaqtingizda ko'proq nima haqida o'rganishni yoqtirasiz?",
        "options": [
            ("🤖 Yangi texnologiyalar, gadjetlar, sun'iy intellekt va dasturlar", "tech"),
            ("🧠 Psixologiya, inson munosabatlari va shaxsiy tarbiya", "people"),
            ("🎬 San'at, dizayn, arxitektura, musiqa yoki adabiyot", "creative"),
            ("💰 Moliya, investitsiyalar, mashhur tadbirkorlar va muvaffaqiyat sirlari", "business")
        ]
    }
]

CAREER_PROFILES = {
    "tech": {
        "title": "💻 IT, Texnologiya va Mantiqiy Tahlil Yo'nalishi",
        "desc": "Sizda kuchli tahliliy fikrlash, diqqatni bir joyga jamlay olish va tizimli yondashuv mavjud. Texnologiyalar orqali muammolarni hal qilish siz uchun ideal yo'ldir.",
        "careers": [
            {
                "name": "Backend / Frontend Dasturchi (Software Engineer)",
                "desc": "Veb-saytlar, mobil ilovalar va yirik tizimlarning ichki yoki tashqi qismini yaratadi.",
                "why": "Mantiqiy fikrlash va muammolarni kod orqali yechish sizga zavq beradi.",
                "skills": "Python, JavaScript, SQL, Git, algoritmlar."
            },
            {
                "name": "Ma'lumotlar Tahlilchisi (Data Analyst / Data Scientist)",
                "desc": "Katta hajmdagi ma'lumotlarni tahlil qilib, biznes va jamiyat uchun muhim xulosalar chiqaradi.",
                "why": "Raqamlar ortidagi qonuniyatlarni ko'ra olish qobiliyatingiz yuqori.",
                "skills": "Python (Pandas, NumPy), Excel, SQL, Tableau / PowerBI."
            },
            {
                "name": "Kiberxavfsizlik Mutaxassisi (Cybersecurity Specialist)",
                "desc": "Kompaniya va davlat tizimlarini xakerlik hujumlari va ma'lumot o'g'irlanishidan himoya qiladi.",
                "why": "Zehnli ekanligingiz va xavfsizlikka mas'uliyatli yondashuvingiz mos keladi.",
                "skills": "Tarmoq protokollari, Linux, xavfsizlik auditlari, kriptografiya."
            },
            {
                "name": "Sun'iy Intellekt va Prompt Muhandisi (AI / LLM Engineer)",
                "desc": "Zamonaviy AI modellarini biznes jarayonlariga joriy etadi va ularni o'rgatadi.",
                "why": "Kelajak texnologiyalariga qiziqishingiz va tez o'rgana olishingiz ustunlik beradi.",
                "skills": "Machine Learning asoslari, Python, API integratsiyalari."
            }
        ],
        "roadmap": "Dastlab Python asoslarini o'rganishdan boshlang, kichik amaliy loyihalar qiling va GitHub portfolio yarating."
    },
    "people": {
        "title": "👥 Insonlar Bilan Ishlash, Ta'lim va Psixologiya Yo'nalishi",
        "desc": "Sizda yuqori empatiya, boshqalarni tushunish, tinglash va qo'llab-quvvatlash iqtidori bor. Odamlar bilan muloqot orqali ularga foyda keltirish sizning kuchli tomoningiz.",
        "careers": [
            {
                "name": "Psixologik Maslahatchi / Kouch (Life & Career Coach)",
                "desc": "Insonlarga hayotiy qiyinchiliklarni yengish, maqsad qo'yish va ruhiy xotirjamlik topishga yordam beradi.",
                "why": "Siz tinglashni bilasiz va odamlarning qalbini his qila olasiz.",
                "skills": "Faol tinglash, kognitiv-xulqiy terapiya asoslari, empatiya, suhbat san'ati."
            },
            {
                "name": "Inson Resurslari Mutaxassisi (HR Manager / Recruiter)",
                "desc": "Kompaniyaga iqtidorli kadrlarni jalb qiladi, jamoaviy muhitni sog'lom saqlaydi.",
                "why": "Insonlarning kuchli tomonlarini darhol ilg'aysiz va to'g'ri muloqot o'rnatasiz.",
                "skills": "Intervyu o'tkazish, jamoa psixologiyasi, mehnat qonunchiligi."
            },
            {
                "name": "Zamonaviy Murabbiy / Metodist (Corporate Trainer / EdTech)",
                "desc": "Zamonaviy o'quv dasturlarini ishlab chiqadi, xodimlar va talabalarga ko'nikmalar o'rgatadi.",
                "why": "Murakkab narsalarni sodda qilib tushuntirish va ilhomlantirish qobiliyatingiz bor.",
                "skills": "Pedagogika, taqdimot san'ati, o'quv kurslari arxitekturasi."
            },
            {
                "name": "Mijozlar Muvaffaqiyati Menejeri (Customer Success Manager)",
                "desc": "Yirik mijozlarning kompaniya mahsulotidan maksimal natija olishiga hamrohlik qiladi.",
                "why": "Xushmuomalalik va muammolarni do'stona hal qilish iqtidoringiz yuqori.",
                "skills": "Muzokaralar, muammoli vaziyatlarni boshqarish, CRM tizimlari."
            }
        ],
        "roadmap": "Muloqot psixologiyasi bo'yicha kitoblar o'qing, notiqlik san'atini rivojlantiring va jamoat loyihalarida ko'ngilli bo'lib tajriba orttiring."
    },
    "creative": {
        "title": "🎨 Ijod, Dizayn, Media va San'at Yo'nalishi",
        "desc": "Sizda boy tasavvur, nozik did va erkin ijodiy fikrlash bor. Bir xillikdan qochib, o'ziga xos va esda qolarli narsalar yaratishga intilasiz.",
        "careers": [
            {
                "name": "UI/UX Dizayner (Product & Interface Designer)",
                "desc": "Mobil ilovalar va saytlarning qulay, chiroyli va tushunarli ko'rinishini loyihalashtiradi.",
                "why": "Gozallik bilan qulaylikni birlashtirish iste'dodingiz ayni muddao.",
                "skills": "Figma, foydalanuvchi psixologiyasi, kompozitsiya, prototiplash."
            },
            {
                "name": "Kopirayter va Storyteller (Content Creator)",
                "desc": "Insonlar qalbiga yetib boruvchi maqolalar, reklama matnlari va ssenariylar yozadi.",
                "why": "Fikrlarni so'zlar orqali chiroyli va ta'sirli ifodalay olasiz.",
                "skills": "Savodli yozuv, hikoyachilik (storytelling), marketing psixologiyasi."
            },
            {
                "name": "Grafik Dizayner va Brending Mutaxassisi",
                "desc": "Logotiplar, brend uslubi va vizual qiyofalarni yaratadi.",
                "why": "Ranglar, shakllar va vizual uyg'unlikni nozik his qilasiz.",
                "skills": "Adobe Photoshop, Illustrator, brend arxitekturasi, tipografika."
            },
            {
                "name": "Video Montajchi va Motion Dizayner (Video Editor)",
                "desc": "Kino, YouTube va ijtimoiy tarmoqlar uchun dinamik, jozibali videolar tayyorlaydi.",
                "why": "Dinamika, ritm va vizual effektlar orqali hissiyot uyg'ota olasiz.",
                "skills": "Adobe Premiere Pro, After Effects, CapCut, rang tuzatish (color grading)."
            }
        ],
        "roadmap": "Figma yoki dizayn dasturlarini o'rganishni boshlang, Behance/Dribbble saytlarida o'z ishlaringiz portfoliyosini to'plang."
    },
    "business": {
        "title": "📈 Biznes, Loyiha Boshqaruvi va Tadbirkorlik Yo'nalishi",
        "desc": "Sizda strategik maqsadlar qo'yish, natijaga erishish va resurslarni unumli boshqarish qobiliyati kuchli. Mustaqil qaror qabul qilishdan va xatarlardan qo'rqmaysiz.",
        "careers": [
            {
                "name": "Loyiha Menejeri (Project Manager / Scrum Master)",
                "desc": "Jamoani birlashtirib, loyihani belgilangan muddat va byudjet ichida muvaffaqiyatli yakunlaydi.",
                "why": "Tashkilotchilik, nazorat va rejalashtirish qobiliyatingiz a'lo darajada.",
                "skills": "Agile/Scrum metodologiyalari, Jira/Trello, vaqt boshqaruvi, muzokaralar."
            },
            {
                "name": "Mahsulot Menejeri (Product Manager)",
                "desc": "Bozor talabini o'rganib, foydalanuvchilar sevib ishlatadigan mahsulotlarni yaratishga boshchilik qiladi.",
                "why": "Biznes mantiq, foydalanuvchi ehtiyoji va texnologiyalarni bog'lay olasiz.",
                "skills": "Bozor tahlili, A/B testlar, mijozlar bilan intervyu, strategik rejalash."
            },
            {
                "name": "Raqamli Marketing va Sotuvlar Rahbari (Marketing Lead)",
                "desc": "Mahsulotni bozorga olib chiqadi, reklama kampaniyalarini boshqaradi va daromadni oshiradi.",
                "why": "Ishontirish, sotuv san'ati va raqamli kanallarni tushunish sizga mos.",
                "skills": "Targeting, Google Ads, Analytics, sotuv voronkalari."
            },
            {
                "name": "Tadbirkor / Startap Asoschisi (Founder)",
                "desc": "O'z g'oyasini real biznesga aylantirib, yangi ish o'rinlari va qiymat yaratadi.",
                "why": "Xatarlardan qo'rqmaslik, qat'iyatlilik va mustaqillik ruhingiz bor.",
                "skills": "Moliyaviy rejalashtirish, jamoa yig'ish, sotuvlar, qat'iyat."
            }
        ],
        "roadmap": "Biznes va loyiha boshqaruvi kitoblarini (Scrum, Lean Startup) o'qing, kichik tijoriy loyiha boshlab amaliy tajriba orttiring."
    }
}
