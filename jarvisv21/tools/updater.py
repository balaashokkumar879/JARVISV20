"""
=========================================
SYSTEM HEALTH CHECK
=========================================
"""

import shutil
import platform
import subprocess


class Updater:

    def python(self):

        return platform.python_version()

    # -------------------------

    def ollama(self):

        try:

            result = subprocess.run(

                ["ollama", "--version"],

                capture_output=True,

                text=True

            )

            return result.stdout.strip()

        except:

            return "Not Installed"

    # -------------------------

    def tesseract(self):

        return shutil.which("tesseract") is not None

    # -------------------------

    def report(self):

        return {

            "python": self.python(),

            "ollama": self.ollama(),

            "tesseract": self.tesseract()

        }


updater = Updater()