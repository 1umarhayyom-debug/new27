import sys
from guardrails import check_guardrails
from ai_service import SYSTEM_PROMPT

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

def test_guardrails():
    print("=== 1. Guardrails (Xavfsizlik va yo'naltirish) testlari ===")
    
    # A) Muammoni aniqlashtirish testi
    vague_inputs = [
        "muammom bor",
        "qiynalib ketdim",
        "yordam bering",
        "maslahat kerak"
    ]
    for inp in vague_inputs:
        res = check_guardrails(inp)
        assert res is not None and res["type"] == "clarify_problem", f"Kutilgan natija clarify_problem, olingan: {res}"
        assert "vaziyatni to'liqroq" in res["response"].lower()
    print("✅ 1. Qisqa/mavhum muammolarda vaziyatni to'liq so'rash tekshiruvi: O'TDI")

    # B) Sog'liq masalalari testi
    health_inputs = [
        "Boshim qattiq og'riyapti nima dori ichsam bo'ladi?",
        "Toshma toshdi va istima chiqdi, qanday tabletka ichish kerak?",
        "Ko'ngil aynishi va oshqozon og'rig'ini davolash yo'li bormi?"
    ]
    for inp in health_inputs:
        res = check_guardrails(inp)
        assert res is not None and res["type"] == "health", f"Kutilgan natija health, olingan: {res}"
        # Tabiiy tavsiya bormi?
        assert "suv" in res["response"].lower() or "havo" in res["response"].lower() or "dush" in res["response"].lower()
        # Shifokorga yo'naltirish bormi?
        assert "shifokor" in res["response"].lower()
    print("✅ 2. Sog'liq masalalarida kichik tabiiy tavsiya + shifokorga yo'naltirish: O'TDI")

    # C) Chuqur diniy masalalar testi
    religion_inputs = [
        "Bu holatda shariat hukmi qanday, fatvo bormi?",
        "Taloq tushadimi yoki yo'qmi?",
        "Bu ish harommi yoki halolmi, hukm bering"
    ]
    for inp in religion_inputs:
        res = check_guardrails(inp)
        assert res is not None and res["type"] == "deep_religion", f"Kutilgan natija deep_religion, olingan: {res}"
        # O'zbek qadriyatlari bormi?
        assert "qadriyat" in res["response"].lower() or "o'zbek" in res["response"].lower()
        # Rasmiy idora yoki ulamolarga yo'naltirish bormi?
        assert "ulamolar" in res["response"].lower() or "musulmonlari idorasi" in res["response"].lower()
    print("✅ 3. Chuqur diniy masalalarda o'zbek qadriyatlari + rasmiy ulamolarga yo'naltirish: O'TDI")

    # D) Oddiy savollarda filtrdan o'tib ketishi testi
    normal_inputs = [
        "Yangi biznes boshlash uchun qanday g'oyalar bera olasiz?",
        "Ikki xil ish taklifi tushdi, qaysi birini tanlashni bilmayapman, qaror qabul qilishga yordam bering",
        "Bugun o'zimni juda charchagan his qilyapman, motivatsiya kerak"
    ]
    for inp in normal_inputs:
        res = check_guardrails(inp)
        assert res is None, f"Oddiy savol filtrda ushlanib qolmasligi kerak edi: {inp}"
    print("✅ 4. Psixologik va qaror qabul qilish bo'yicha savollarning AI mentorga o'tishi: O'TDI")

def test_system_prompt():
    print("\n=== 2. AI System Prompt talablari tekshiruvi ===")
    prompt_lower = SYSTEM_PROMPT.lower()
    
    assert "vaziyatni to'liqroq" in prompt_lower or "izohlashini" in prompt_lower, "Muammoni to'liq so'rash ko'rsatmasi yo'q"
    assert "shifokor" in prompt_lower, "Sog'liqda shifokorga yo'naltirish ko'rsatmasi yo'q"
    assert "neytral" in prompt_lower or "xolis" in prompt_lower, "Siyosatda neytral/xolis javob ko'rsatmasi yo'q"
    assert "o'zbek" in prompt_lower and "qadriyat" in prompt_lower, "Din masalasida o'zbek qadriyatlari ko'rsatmasi yo'q"
    assert "ulamolar" in prompt_lower or "musulmonlari idorasi" in prompt_lower, "Diniy ulamolarga yo'naltirish ko'rsatmasi yo'q"
    
    # Yangi talablar:
    assert "falsafiy" in prompt_lower or "donishmandlik" in prompt_lower, "Falsafiy mushohada ko'rsatmasi yo'q"
    assert "ehtimoliy" in prompt_lower and "oqibat" in prompt_lower, "Ehtimoliy kelib chiquvchi vaziyatlar/ssenariylar prognozi ko'rsatmasi yo'q"
    assert "variant" in prompt_lower and "yechim" in prompt_lower, "Ko'p variantli yechimlar ko'rsatmasi yo'q"
    print("✅ Barcha talablar (falsafiy tahlil, ssenariylar prognozi, ko'p variantli yechimlar, sog'liq/shifokor, siyosat/neytral, din/qadriyat) to'liq mujassamlashgan: O'TDI")

if __name__ == "__main__":
    try:
        test_guardrails()
        test_system_prompt()
        print("\n🎉 Barcha testlar muvaffaqiyatli yakunlandi! Bot to'g'ri sozlangan.")
    except AssertionError as e:
        print(f"\n❌ Test xatoligi: {e}")
        sys.exit(1)
