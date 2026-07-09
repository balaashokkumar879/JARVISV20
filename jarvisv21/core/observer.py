"""
=========================================
JARVIS BACKGROUND OBSERVER
=========================================
"""

import threading
import time

from tools.memory import memory


class Observer:

    def __init__(self):

        self.running = False

        self.thread = None

    # ------------------------------------

    def loop(self):

        while self.running:

            #
            # Future Modules
            #
            # WhatsApp Monitor
            # Vision Monitor
            # Clipboard Monitor
            # Reminder Monitor
            #

            time.sleep(1)

    # ------------------------------------

    def start(self):

        if self.running:

            return

        self.running = True

        self.thread = threading.Thread(

            target=self.loop,

            daemon=True

        )

        self.thread.start()

    # ------------------------------------

    def stop(self):

        self.running = False


observer = Observer()