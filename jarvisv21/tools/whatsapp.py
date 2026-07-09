"""
=========================================
JARVIS WHATSAPP ENGINE V4
=========================================
"""

import time
import pyautogui
import pyperclip

from tools.desktop import desktop


class WhatsApp:

    def __init__(self):

        self.launch_wait = 5

    # ---------------------------------

    def open(self):

        desktop.open("whatsapp")

        time.sleep(self.launch_wait)

    # ---------------------------------

    def search_contact(self, contact):

        self.open()

        pyautogui.hotkey("ctrl", "f")

        time.sleep(0.5)

        pyautogui.hotkey("ctrl", "a")

        pyautogui.press("backspace")

        pyperclip.copy(contact)

        pyautogui.hotkey("ctrl", "v")

        time.sleep(1)

        pyautogui.press("enter")

        time.sleep(1)

    # ---------------------------------

    def send_message(self, contact, message):

        self.search_contact(contact)

        pyperclip.copy(message)

        pyautogui.hotkey("ctrl", "v")

        pyautogui.press("enter")

        return True

    # ---------------------------------

    def send_multiple(self, contacts, message):

        sent = []

        failed = []

        for person in contacts:

            try:

                self.send_message(person, message)

                sent.append(person)

            except Exception:

                failed.append(person)

        return {

            "sent": sent,

            "failed": failed

        }

    # ---------------------------------

    def send_file(self, contact, filepath):

        self.search_contact(contact)

        pyautogui.hotkey("ctrl", "shift", "u")

        time.sleep(1)

        pyperclip.copy(filepath)

        pyautogui.hotkey("ctrl", "v")

        pyautogui.press("enter")

        time.sleep(2)

        pyautogui.press("enter")

        return True

    # ---------------------------------

    def voice_call(self, contact):

        self.search_contact(contact)

        pyautogui.hotkey("ctrl", "shift", "c")

    # ---------------------------------

    def video_call(self, contact):

        self.search_contact(contact)

        pyautogui.hotkey("ctrl", "shift", "v")

    # ---------------------------------

    def type_only(self, contact, message):

        self.search_contact(contact)

        pyperclip.copy(message)

        pyautogui.hotkey("ctrl", "v")

    # ---------------------------------

    def read_last_message(self):

        pyautogui.hotkey("ctrl", "a")

        pyautogui.hotkey("ctrl", "c")

        try:

            return pyperclip.paste()

        except:

            return ""

    # ---------------------------------

    def close(self):

        pyautogui.hotkey("alt", "f4")


whatsapp = WhatsApp()