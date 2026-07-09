"""
=========================================
TASK SCHEDULER
=========================================
"""

import threading
import time


class Scheduler:

    def __init__(self):

        self.tasks = []

    def add(self, seconds, func, *args):

        self.tasks.append(
            (
                time.time() + seconds,
                func,
                args
            )
        )

    def run(self):

        while True:

            now = time.time()

            for task in self.tasks[:]:

                execute, func, args = task

                if now >= execute:

                    try:
                        func(*args)
                    except:
                        pass

                    self.tasks.remove(task)

            time.sleep(1)

    def start(self):

        threading.Thread(

            target=self.run,

            daemon=True

        ).start()


scheduler = Scheduler()