"""
=========================================
JARVIS V21 CONFIGURATION
=========================================
"""

from pathlib import Path

# ===========================
# PROJECT
# ===========================

ROOT = Path(__file__).parent

CORE = ROOT / "core"
TOOLS = ROOT / "tools"
DATA = ROOT / "data"
MODELS = ROOT / "models"

import os
from pathlib import Path

ROOT = Path(__file__).parent

DATA = ROOT / "data"

CACHE = DATA / "cache"

if not os.path.isdir(CACHE):
    os.makedirs(CACHE, exist_ok=True)

# ===========================
# AI
# ===========================

OLLAMA_MODEL = "phi3:mini"

MAX_RESPONSE_WORDS = 40

TEMPERATURE = 0.3

# ===========================
# OCR
# ===========================

TESSERACT_PATH = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# ===========================
# VOICE
# ===========================

VOICE_RATE = 180

VOICE_VOLUME = 1.0

VOICE_ID = 0

# ===========================
# MEMORY
# ===========================

MEMORY_FILE = DATA / "memory.json"

REMINDER_FILE = DATA / "reminders.json"

# ===========================
# SCREEN
# ===========================

SCREENSHOT_INTERVAL = 2

OCR_INTERVAL = 2

# ===========================
# WHATSAPP
# ===========================

WHATSAPP_PROCESS = "WhatsApp.exe"

AUTO_REPLY = False

# ===========================
# PERFORMANCE
# ===========================

MAX_HISTORY = 20

MAX_CACHE = 100

CPU_SLEEP = 0.5