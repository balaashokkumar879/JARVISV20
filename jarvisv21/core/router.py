"""
=========================================
JARVIS SMART ROUTER V5
=========================================
"""

from core.brain import brain
from core.intents import intent_engine

from tools.desktop import desktop
from tools.browser import browser
from tools.whatsapp import whatsapp
from tools.system import system


class Router:

    def __init__(self):
        pass

    # ----------------------------------------

    def handle(self, command: str):

        commands = self.split_commands(command)

        responses = []

        for cmd in commands:

            response = self.handle_single(cmd)

            if response:
                responses.append(response)

        return " ".join(responses)

    # ----------------------------------------

    def split_commands(self, command):

        separators = [

            " and ",

            " then ",

            ","

        ]

        commands = [command]

        for sep in separators:

            temp = []

            for item in commands:

                temp.extend(item.split(sep))

            commands = temp

        return [x.strip() for x in commands if x.strip()]

    # ----------------------------------------

    def handle_single(self, command):

        task = intent_engine.detect(command)

        intent = task["intent"]

        # ------------------------------------
        # OPEN
        # ------------------------------------

        if intent == "OPEN":

            target = task["target"]

            if browser.open(target):

                return f"Opening {target}"

            desktop.open(target)

            return f"Opening {target}"

        # ------------------------------------
        # GOOGLE
        # ------------------------------------

        if intent == "GOOGLE":

            browser.google(task["query"])

            return "Searching Google."

        # ------------------------------------
        # YOUTUBE
        # ------------------------------------

        if intent == "YOUTUBE":

            browser.youtube(task["query"])

            return "Searching YouTube."

        # ------------------------------------
        # MAPS
        # ------------------------------------

        if intent == "MAPS":

            browser.maps(task["place"])

            return "Opening Maps."

        # ------------------------------------
        # WHATSAPP
        # ------------------------------------

        if intent == "WHATSAPP":

            whatsapp.send_message(

                task["contact"],

                task["message"]

            )

            return "Message sent."

        # ------------------------------------
        # CALL
        # ------------------------------------

        if intent == "CALL":

            whatsapp.voice_call(

                task["contact"]

            )

            return "Calling."

        # ------------------------------------
        # VIDEO CALL
        # ------------------------------------

        if intent == "VIDEO_CALL":

            whatsapp.video_call(

                task["contact"]

            )

            return "Video call started."

        # ------------------------------------
        # SYSTEM
        # ------------------------------------

        if intent == "BATTERY":

            return f"Battery is {system.battery()} percent."

        if intent == "CPU":

            return f"CPU usage is {system.cpu()} percent."

        if intent == "RAM":

            return f"RAM usage is {system.ram()} percent."

        # ------------------------------------
        # EXIT
        # ------------------------------------

        if intent == "EXIT":

            return "Goodbye."

        # ------------------------------------
        # AI
        # ------------------------------------

        return brain.ask(task["message"])


router = Router()