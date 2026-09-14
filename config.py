import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
env_path = BASE_DIR / ".env"

try:
    from dotenv import load_dotenv
    load_dotenv(env_path)
except ImportError:
    # Agar python-dotenv o'rnatilmagan bo'lsa, .env faylini to'g'ridan-to'g'ri o'qish
    if env_path.exists():
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    os.environ[key.strip()] = val.strip()

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash").strip()

def validate_config():
    """Sozlamalarning to'g'riligini tekshirish"""
    warnings = []
    if not BOT_TOKEN:
        warnings.append("DIQQAT: BOT_TOKEN ko'rsatilmagan! Bot ishga tushishi uchun .env fayliga Telegram bot tokenini yozing.")
    if not OPENAI_API_KEY and not GEMINI_API_KEY:
        warnings.append("ESLATMA: OPENAI_API_KEY yoki GEMINI_API_KEY ko'rsatilmagan! Bot demo rejimida ishlaydi.")
    return warnings
