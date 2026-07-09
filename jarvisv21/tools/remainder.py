"""
=========================================
REMINDER ENGINE
=========================================
"""

import json

from config import REMINDER_FILE


class Reminder:

    def __init__(self):

        self.tasks = []

        self.load()

    # ----------------------------

    def load(self):

        try:

            with open(

                REMINDER_FILE,

                "r",

                encoding="utf-8"

            ) as f:

                self.tasks = json.load(f)

        except:

            self.tasks = []

    # ----------------------------

    def save(self):

        with open(

            REMINDER_FILE,

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                self.tasks,

                f,

                indent=4

            )

    # ----------------------------

    def add(self, title, when):

        self.tasks.append(

            {

                "title": title,

                "time": when

            }

        )

        self.save()

    # ----------------------------

    def all(self):

        return self.tasks


reminder = Reminder()