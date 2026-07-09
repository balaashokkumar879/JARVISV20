"""
=========================================
JARVIS ASSISTANT
=========================================
"""

from core.voice import Voice

from core.router import Router

from core.services import Services


class Assistant:

    def __init__(self):

        self.voice = Voice()

        self.router = Router()

        self.services = Services()

    # ----------------------------------

    def start(self):

        print("=" * 50)
        print("JARVIS V21")
        print("=" * 50)

        self.services.start()

        self.voice.speak("Jarvis is online.")

        while True:

            command = self.voice.listen()

            if not command:
                command = self.voice.keyboard()

            if not command:
                continue

            response = self.router.handle(command)

            if response:
                self.voice.speak(response)

            if command.lower() in [

                "exit",
                "quit",
                "stop"

            ]:

                break

        self.services.stop()
        