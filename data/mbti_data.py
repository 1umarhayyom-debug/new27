"""
data/mbti_data.py - MBTI (Myers-Briggs) xarakter testi savollari va 16 ta tip tahlili.
"""

MBTI_QUESTIONS = [
    # 1. Ekstraversiya (E) vs Introversiya (I)
    {
        "id": 1,
        "dimension": "EI",
        "question": "Og'ir va charchoqli haftadan so'ng quvvatingizni qanday tiklaysiz?",
        "option_a": ("Ko'pchilik do'stlar bilan uchrashib, shovqinli davrada gaplashib", "E"),
        "option_b": ("Yolg'iz qolib, kitob o'qib, kino ko'rib yoki tinch dam olib", "I")
    },
    {
        "id": 2,
        "dimension": "EI",
        "question": "Yangi jamoa yoki notanish davraga tushib qolsangiz:",
        "option_a": ("Osonlikcha yangi insonlar bilan birinchi bo'lib suhbat boshlayman", "E"),
        "option_b": ("Biroz chetdan kuzataman va faqat o'zimga yaqin his qilganlar bilan gaplashaman", "I")
    },
    # 2. Sensorika/Sezgi (S) vs Intuitsiya (N)
    {
        "id": 3,
        "dimension": "SN",
        "question": "Ma'lumotlarni qabul qilishda sizga qaysi biri ko'proq yoqadi?",
        "option_a": ("Aniq faktlar, hayotiy misollar va amaliy tajriba", "S"),
        "option_b": ("Keng g'oyalar, kelajak imkoniyatlari va falsafiy ma'nolar", "N")
    },
    {
        "id": 4,
        "dimension": "SN",
        "question": "Biror narsani tasavvur qilganda:",
        "option_a": ("Hozir va shu yerda bor narsalarga, real holatga tayanaman", "S"),
        "option_b": ("Kelajakda nima bo'lishi mumkinligi va yashirin ma'nolarni qidiraman", "N")
    },
    # 3. Mantiq/Tafakkur (T) vs His-tuyg'u (F)
    {
        "id": 5,
        "dimension": "TF",
        "question": "Muhim qaror qabul qilishda nima siz uchun birinchi o'rinda turadi?",
        "option_a": ("Sovuqqon mantiq, adolat, qoidalar va obyektiv hisob-kitob", "T"),
        "option_b": ("Insoniy munosabatlar, mehr-oqibat, qadriyatlar va yurak amri", "F")
    },
    {
        "id": 6,
        "dimension": "TF",
        "question": "Do'stingiz xato qilganini ko'rsangiz:",
        "option_a": ("Vaziyatni to'g'rilash uchun xatosini ochiq va mantiqan tushuntiraman", "T"),
        "option_b": ("Ko'nglini og'ritmaslik uchun avval uni qo'llab-quvvatlab, yumshoq aytaman", "F")
    },
    # 4. Rejalilik (J) vs Moslashuvchanlik (P)
    {
        "id": 7,
        "dimension": "JP",
        "question": "Kundalik ishlaringiz va hayotingiz qanday tashkillashtirilgan?",
        "option_a": ("Aniq reja, ro'yxat va jadval asosida — oldindan rejalashtirishni yoqtiraman", "J"),
        "option_b": ("Spontan va erkin — vaziyatga qarab o'zgaruvchan harakat qilish yoqadi", "P")
    },
    {
        "id": 8,
        "dimension": "JP",
        "question": "Biror vazifani bajarishda:",
        "option_a": ("Muddatidan oldin, bosqichma-bosqich qilib qo'yib, xotirjam bo'lishni xohlayman", "J"),
        "option_b": ("Ko'pincha oxirgi daqiqalarda ilhom va bosim ostida eng yaxshi natijaga erishaman", "P")
    }
]

MBTI_PROFILES = {
    "INTJ": {
        "title": "INTJ — Strateg va Me'mor (The Mastermind)",
        "desc": "Mustaqil, chuqur fikrlovchi va uzoqni ko'ra oladigan strateg. Siz har bir ishda tizim, mantiq va mukammallikni qadrlaysiz.",
        "strengths": ["Strategik fikrlash", "Yuqori mustaqillik", "Chuqur tahlil va qat'iyatlilik", "Murakkab tizimlarni soddalashtirish"],
        "weaknesses": ["Haddan tashqari tanqidiy bo'lish", "Boshqalarning his-tuyg'ularini ba'zan e'tiborsiz qoldirish", "Murosasizlik"],
        "careers": ["Dasturiy arxitektor / Senior Dasturchi", "Strategik boshqaruvchi", "Moliya tahlilchisi", "Ilmiy tadqiqotchi"],
        "advice": "Ba'zan reja bo'yicha ketmaslik ham go'zallik keltiradi. Atrofdagilar bilan his-tuyg'ular orqali ham muloqot qilishni unutmang."
    },
    "INTP": {
        "title": "INTP — Olim va Mantiqchi (The Thinker)",
        "desc": "Cheksiz qiziquvchan, nazariyotchi va kashfiyotchi. Yangi g'oyalar va muammolarning ichki mohiyatini tushunish sizning asosiy ehtirosingizdir.",
        "strengths": ["Mantiqiy chuqurlik", "Nostandart fikrlash", "Ob'ektiv tahlil", "Murakkab abstrakt tushunchalarni oson ilg'ash"],
        "weaknesses": ["Rejalarni oxiriga yetkazmaslik", "Kundalik amaliy mayda ishlarni yoqtirmaslik", "Haddan tashqari xayolparastlik"],
        "careers": ["Sun'iy intellekt muhandisi", "Falsafachi / Nazariyotchi", "Kiberxavfsizlik mutaxassisi", "Ma'lumotlar olimi (Data Scientist)"],
        "advice": "Buyuk g'oyalaringiz hayotga ko'chishi uchun ularni kichik amaliy qadamlarga bo'lib, oxirigacha amalga oshirishni odat qiling."
    },
    "ENTJ": {
        "title": "ENTJ — Qo'mondon va Lider (The Commander)",
        "desc": "Tug'ma rahbar, dadil va qat'iyatli. Katta maqsadlar qo'yib, jamoani o'z ortidan ergashtirishda tengsizsiz.",
        "strengths": ["Liderlik qobiliyati", "Kuchli iroda va intizom", "Tez va aniq qaror qabul qilish", "Strategik ko'rish"],
        "weaknesses": ["Sabrsizlik", "Boshqalarning sustkashligiga nisbatan qattiqqo'llik", "Hissiyotlarni chetga surish"],
        "careers": ["Bosh direktor (CEO) / Biznes asoschisi", "Katta loyiha boshqaruvchisi", "Investitsiya tahlilchisi", "Boshqaruv konsaltingi"],
        "advice": "Haqiqiy kuch — faqat buyruq berishda emas, balki atrofdagilarni tushunish va ularni ilhomlantirishda hamdir."
    },
    "ENTP": {
        "title": "ENTP — Ixtirochi va Bahslashuvchi (The Visionary)",
        "desc": "Zukko, chaqqon fikrlovchi va doimo yangilik qidiruvchi innovator. Siz qoliplarni buzishni va yangi imkoniyatlarni kashf etishni yoqtirasiz.",
        "strengths": ["Kreativlik va g'oyalar chaqnashi", "Tez moslashuvchanlik", "Qoyilmaqom notiqlik", "Murakkab masalalarga noodatiy yechim topish"],
        "weaknesses": ["Bir ishni tugatmay ikkinchisiga o'tib ketish", "Baho berishda haddan tashqari bahslashish", "Rutina va bir xillikdan tez zerikish"],
        "careers": ["Startap asoschisi", "Kreativ direktor", "Mahsulot boshqaruvchisi (Product Manager)", "Siyosiy / Strategik maslahatchi"],
        "advice": "Sizda g'oyalar daryodek toshadi. Eng muhim 1-2 ta g'oyangizni tanlab, uni to'liq tugatishga intizom bilan yondashing."
    },
    "INFJ": {
        "title": "INFJ — Maslahatchi va Himoyachi (The Advocate)",
        "desc": "Kamdan-kam uchraydigan, chuqur ma'naviyatli va idealist shaxs. Insonlarga yordam berish va dunyoni yaxshiroq qilish sizning hayotiy missiyangizdir.",
        "strengths": ["Kuchli empatiya va sezgi", "Yuksak qadriyatlar va tamoyillar", "Ijodkorlik", "Insonlarning ichki dunyosini darhol anglash"],
        "weaknesses": ["Boshqalarning dardini o'ziga olib tez toliqish (burnout)", "Perfeksionizm", "O'zini juda yopiq tutish"],
        "careers": ["Psixolog / Psixoterapevt", "Yozuvchi / Ssenarist", "Inson resurslari (HR) direktori", "Ijtimoiy loyihalar yetakchisi"],
        "advice": "Boshqalarni qutqarishdan oldin o'z ruhiy va jismoniy holatingizga g'amxo'rlik qilishni unutmang. O'zingizga ham mehr bering."
    },
    "INFP": {
        "title": "INFP — Vositachi va Idealist (The Mediator)",
        "desc": "Hissiyotga boy, mehribon va ichki dunyosi go'zal shaxs. O'z qadriyatlariga sadoqatli va har bir insonda yaxshilikni ko'ra oladi.",
        "strengths": ["Samimiylik va chuqur mehr", "Kuchli badiiy tasavvur", "Mustaqil dunyoqarash", "Empatiya va tinglash san'ati"],
        "weaknesses": ["Tanqidni juda og'ir qabul qilish", "Haddan tashqari xayolga berilish", "Amaliy qadamlarni kechiktirish"],
        "careers": ["Yozuvchi / Jurnalist", "Grafik dizayner / Rassom", "Psixologik maslahatchi", "Ma'naviy-ma'rifiy soha mutaxassisi"],
        "advice": "Ichki go'zalligingiz va g'oyalaringizni dunyodan yashirmang. O'z iste'dodingizga ishoning va birinchi qadamni dadil tashlang."
    },
    "ENFJ": {
        "title": "ENFJ — Murabbiy va Yo'lboshchi (The Protagonist)",
        "desc": "Xarizmatik, iliq va ilhomlantiruvchi yetakchi. Insonlarning iqtidorini ochishga va jamoani umumiy ezgu maqsad atrofida birlashtirishga usta.",
        "strengths": ["Ajoyib notiqlik", "Kuchli empatiya va odamlarni birlashtirish", "Mas'uliyatlilik", "Ijobiy energiya tarqatish"],
        "weaknesses": ["Hamma uchun javobgarlikni bo'yniga olish", "O'z ehtiyojlarini unutib yuborish", "Haddan tashqari ta'sirchanlik"],
        "careers": ["Murabbiy (Coach) / Trener", "Jamoatchilik bilan aloqalar (PR) rahbari", "Ta'lim sohasi yetakchisi", "Tashkilotchi / Menejer"],
        "advice": "Ba'zan 'yo'q' deyishni ham o'rganing. O'z kuchingizni faqat chin dildan arziydigan ezgu ishlarga sarflang."
    },
    "ENFP": {
        "title": "ENFP — Ilhomlantiruvchi va Chempion (The Campaigner)",
        "desc": "Hayotga oshiq, jo'shqin va ijodkor shaxs. Har bir insonda va har bir vaziyatda cheksiz imkoniyatlarni ko'radi.",
        "strengths": ["Yuqori kommunikatsiya", "Ijodiy erkinlik", "Odamlarni ruhlantirish", "Qiziquvchanlik va ochiqko'ngillik"],
        "weaknesses": ["Diqqatni bir joyga jamlash qiyinligi", "Tartib-intizomdan qochish", "Ortiqcha emotsionallik"],
        "careers": ["Marketolog / Kreativ direktor", "Bloger / Media mutaxassisi", "Tadbirkor / Loyiha muallifi", "Tadbir tashkilotchisi"],
        "advice": "Ilhom kelishini kutmang, intizomni yo'lga qo'ying. Kichik kun tartibi sizning erkinligingizni cheklamaydi, aksincha unumdor qiladi."
    },
    "ISTJ": {
        "title": "ISTJ — Nazoratchi va Mas'uliyat Egasi (The Inspector)",
        "desc": "Ishonchli, bosiq, tartibli va so'zining ustidan chiqadigan inson. Jamiyatning va oilaning mustahkam suyanchig'i.",
        "strengths": ["Halollik va sadoqat", "Ajoyib intizom va tartib", "Aniqlik va faktlarga tayanish", "Vazifalarni vaqtida bajarish"],
        "weaknesses": ["O'zgarishlarga qiyin moslashish", "Qoidalarga qat'iy yopishib olish", "Boshqalarni tushunishda biroz qattiqqo'llik"],
        "careers": ["Bosh hisobchi / Auditor", "Dasturiy ta'minot sifatini nazorat qiluvchi (QA)", "Yurist / Huquqshunos", "Bank boshqaruvchisi"],
        "advice": "Ba'zan rejalardan chetga chiqish yangi yaxshiliklarga yo'l ochadi. Kutilmagan hodisalarni ham tabassum bilan kutib oling."
    },
    "ISFJ": {
        "title": "ISFJ — Himoyachi va Mehribon G'amxo'r (The Defender)",
        "desc": "Kamtarin, mehribon, o'ta mas'uliyatli va atrofdagilarga g'amxo'r inson. Jimjitlik bilan buyuk yaxshiliklarni amalga oshiradi.",
        "strengths": ["Fidoyilik va g'amxo'rlik", "Tafsilotlarga e'tibor", "Amaliy ko'mak ko'rsatish", "Barqarorlik va ishonchlilik"],
        "weaknesses": ["O'z his-tuyg'ularini ichiga yutish", "O'zgartirishlardan xavotirlanish", "O'z mehnati qadrini past baholash"],
        "careers": ["Shifokor / Hamshira", "Boshlang'ich ta'lim o'qituvchisi", "Mijozlar bilan ishlash bo'yicha mutaxassis", "Ofis boshqaruvchisi"],
        "advice": "Siz boshqalarga g'amxo'rlik qilasiz, ammo o'zingizning orzularingiz va hordig'ingiz ham muhim. O'z qadringizni biling."
    },
    "ESTJ": {
        "title": "ESTJ — Tashkilotchi va Boshqaruvchi (The Executive)",
        "desc": "Tartib, qoida va an'analarni hurmat qiluvchi amaliy yetakchi. Har qanday chalkashlikda darhol intizom o'rnatadi.",
        "strengths": ["Kuchli tashkilotchilik", "Halol va to'g'riso'zlik", "Yuqori samaradorlik", "Qat'iyatlilik"],
        "weaknesses": ["Moslashuvchanlikning yetishmasligi", "Boshqalarning his-tuyg'ularini hisobga olmaslik", "O'z fikrini yagona to'g'ri deb bilish"],
        "careers": ["Operatsion direktor (COO)", "Ishlab chiqarish rahbari", "Huquq-tartibot organlari mutaxassisi", "Loyihalar koordinatori"],
        "advice": "Insonlar bilan ishlashda qat'iyat bilan birga samimiyat va tinglash ham juda muhimdir. Hammaning o'z tezligi borligini qabul qiling."
    },
    "ESFJ": {
        "title": "ESFJ — Elchi va Qalbi Daryo Hamroh (The Consul)",
        "desc": "Ochiqko'ngil, mehmondo'st va jamoatparvar. Doimo boshqalarning kayfiyatini ko'tarishga va iliq muhit yaratishga intiladi.",
        "strengths": ["Ajoyib muloqot va mehmondo'stlik", "G'amxo'rlik va sodiqlik", "Jamoada do'stona muhit yaratish", "Amaliy yordam"],
        "weaknesses": ["Boshqalarning fikriga haddan tashqari bog'liq bo'lish", "Ijtimoiy maqomdan xavotirlanish", "Yolg'izlikni yoqtirmaslik"],
        "careers": ["HR menejer / Recruiter", "Jamoatchilik tadbirlari koordinatori", "O'qituvchi / Murabbiy", "Mijozlar xizmati rahbari"],
        "advice": "Hamma sizdan rozi bo'lishi shart emas. Eng avvalo o'z ichki ovozingiz va vijdoningizga quloq tuting."
    },
    "ISTP": {
        "title": "ISTP — Usta va Amaliyotchi (The Virtuoso)",
        "desc": "Bosiq, zehnli va qo'llari bilan narsalarni tuzatishni yoqtiruvchi tahlilchi. Amaliy muammolarga darhol yechim topadi.",
        "strengths": ["Krizis vaziyatlarda xotirjamlik", "Amaliy zehn va qo'l mehnati", "Mantiqiy muammolarni yechish", "Mustaqillik"],
        "weaknesses": ["Boshqalar bilan his-tuyg'ularini bo'lishmaslik", "Tez zerikish", "Uzoq muddatli majburiyatlardan qochish"],
        "careers": ["Muhandis / Mexanik", "Dasturchi / DevOps muhandisi", "Favqulodda vaziyatlar mutaxassisi", "Tizim ma'muri (SysAdmin)"],
        "advice": "Yaqinlaringiz sizning his-tuyg'ularingizni bilishni xohlashadi. Sukut saqlash o'rniga, ichki fikrlaringizni ochiqroq aytib turing."
    },
    "ISFP": {
        "title": "ISFP — Rassom va Ijodkor (The Adventurer)",
        "desc": "Nozik didli, xushmuomala, go'zallikni sevuvchi va erkin ruhli inson. Hayotni har lahzada his qilib yashaydi.",
        "strengths": ["Badiiy did va estetika", "Bag'rikenglik va xushfe'llik", "Erkin fikrlash", "Boshqalarni boricha qabul qilish"],
        "weaknesses": ["Uzoq muddatli rejalashtirishni yoqtirmaslik", "Tanqidga o'ta ta'sirchanlik", "O'z qobiliyatlariga shubha qilish"],
        "careers": ["UI/UX Dizayner", "Fotograf / Rassom", "Modelyer / Stilist", "Pazandachilik / Restoran san'ati"],
        "advice": "Iste'dodingizni tartibli mehnat bilan birlashtirsangiz, haqiqiy durdona asarlar va muvaffaqiyatga erishasiz."
    },
    "ESTP": {
        "title": "ESTP — Harakatchan Tadbirkor (The Entrepreneur)",
        "desc": "Dadil, chaqqon, xavf-xatardan qo'rqmaydigan va har doim voqealar markazida bo'luvchi inson. Harakatda baraka ko'radi.",
        "strengths": ["Tezkor reaktsiya va amaliy yechim", "Yuqori joziba va ishontirish san'ati", "Xatarlarni boshqarish", "Reallikni to'g'ri baholash"],
        "weaknesses": ["Sabrsizlik va rejasiz harakat", "Hissiy chuqurlikdan qochish", "Kelajak oqibatlarini o'ylamaslik"],
        "careers": ["Tadbirkor / Savdo bo'yicha direktor", "Bozor tahlilchisi / Broker", "Sport murabbiyi", "Favqulodda krizis menejeri"],
        "advice": "Tezkorlik yaxshi, lekin katta sakrashdan oldin oldingizdagi to'siqlarni puxta hisob-kitob qilishni odat qiling."
    },
    "ESFP": {
        "title": "ESFP — Quvnoq Sa'natkor (The Entertainer)",
        "desc": "Hayotga zavq bag'ishlovchi, saxiy, hazilkash va atrofdagilarga shodlik ulashuvchi inson. Har bir kunni bayramga aylantira oladi.",
        "strengths": ["Yuqori optimizm va energiya", "Odamlarni o'ziga jalb qilish", "Amaliy yordam", "Estetik zavq va did"],
        "weaknesses": ["Jiddiy muammolardan qochish", "Pul va vaqtni boshqarishda sustlik", "Uzoq muddatli rejalarga qiziqmaslik"],
        "careers": ["Boshlovchi / Aktyor", "Turizm va mehmondo'stlik menejeri", "Sotuvlar bo'yicha yetakchi", "Bolalar rivojlanish mutaxassisi"],
        "advice": "Bugungi quvonch bilan birga kelajak poydevorini ham mustahkamlang. Kichik tejash va rejalashtirish sizni yanada erkin qiladi."
    }
}
