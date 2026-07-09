"""
=========================================
JARVIS SMART INTENT ENGINE V3
=========================================
"""

import re


class IntentEngine:

    def detect(self, command):

        text = command.strip()
        lower = text.lower()

        # -----------------------------
        # OPEN
        # -----------------------------

        if lower.startswith("open "):

            return {
                "intent": "OPEN",
                "target": text[5:].strip()
            }

        # -----------------------------
        # GOOGLE SEARCH
        # -----------------------------

        if lower.startswith("search "):

            return {
                "intent": "GOOGLE",
                "query": text[7:].strip()
            }

        if lower.startswith("google "):

            return {
                "intent": "GOOGLE",
                "query": text[7:].strip()
            }

        # -----------------------------
        # YOUTUBE SEARCH
        # -----------------------------

        if lower.startswith("youtube "):

            return {
                "intent": "YOUTUBE",
                "query": text[8:].strip()
            }

        # -----------------------------
        # MAPS
        # -----------------------------

        if lower.startswith("maps "):

            return {
                "intent": "MAPS",
                "place": text[5:].strip()
            }

        # -----------------------------
        # SEND MESSAGE
        # -----------------------------

        match = re.search(r"send (.+) to (.+)", text, re.IGNORECASE)

        if match:

            return {
                "intent": "WHATSAPP",
                "message": match.group(1).strip(),
                "contact": match.group(2).strip()
            }

        match = re.search(r"tell (.+) (.+)", text, re.IGNORECASE)

        if match:

            return {
                "intent": "WHATSAPP",
                "contact": match.group(1).strip(),
                "message": match.group(2).strip()
            }

        match = re.search(r"message (.+) (.+)", text, re.IGNORECASE)

        if match:

            return {
                "intent": "WHATSAPP",
                "contact": match.group(1).strip(),
                "message": match.group(2).strip()
            }

        # -----------------------------
        # CALL
        # -----------------------------

        if lower.startswith("call "):

            return {
                "intent": "CALL",
                "contact": text[5:].strip()
            }

        # -----------------------------
        # VIDEO CALL
        # -----------------------------

        if lower.startswith("video call "):

            return {
                "intent": "VIDEO_CALL",
                "contact": text[11:].strip()
            }

        # -----------------------------
        # SYSTEM
        # -----------------------------

        if "battery" in lower:

            return {
                "intent": "BATTERY"
            }

        if "cpu" in lower:

            return {
                "intent": "CPU"
            }

        if "ram" in lower:

            return {
                "intent": "RAM"
            }

        # -----------------------------
        # EXIT
        # -----------------------------

        if lower in [
            "exit",
            "quit",
            "stop"
        ]:

            return {
                "intent": "EXIT"
            }

        # -----------------------------
        # AI
        # -----------------------------

        return {
            "intent": "AI",
            "message": text
        }


intent_engine = IntentEngine()