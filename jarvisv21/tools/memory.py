"""
=========================================
MEMORY ENGINE
=========================================
"""

import json

from config import MEMORY_FILE


class Memory:

    def __init__(self):

        self.data = {}

        self.load()

    # -----------------------------

    def load(self):

        try:

            with open(

                MEMORY_FILE,

                "r",

                encoding="utf-8"

            ) as f:

                self.data = json.load(f)

        except Exception:

            self.data = {}

    # -----------------------------

    def save(self):

        with open(

            MEMORY_FILE,

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                self.data,

                f,

                indent=4

            )

    # -----------------------------

    def remember(

        self,

        key,

        value

    ):

        self.data[key] = value

        self.save()

    # -----------------------------

    def recall(

        self,

        key,

        default=None

    ):

        return self.data.get(

            key,

            default

        )

    # -----------------------------

    def forget(self, key):

        if key in self.data:

            del self.data[key]

            self.save()


memory = Memory()