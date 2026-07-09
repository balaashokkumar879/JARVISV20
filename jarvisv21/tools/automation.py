"""
=========================================
AUTOMATION ENGINE
=========================================
"""

import time
import pyautogui
import pyperclip


class Automation:

    def click(self, x, y):

        pyautogui.moveTo(
            x,
            y,
            duration=0.2
        )

        pyautogui.click()

    # -----------------------------

    def write(self, text):

        pyperclip.copy(text)

        pyautogui.hotkey("ctrl", "v")

    # -----------------------------

    def press(self, key):

        pyautogui.press(key)

    # -----------------------------

    def hotkey(self, *keys):

        pyautogui.hotkey(*keys)

    # -----------------------------

    def wait(self, seconds):

        time.sleep(seconds)

    # -----------------------------

    def screenshot(self):

        return pyautogui.screenshot()


automation = Automation()