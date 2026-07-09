"""
=========================================
JARVIS DESKTOP ENGINE V3
=========================================
"""

import os
import time
import webbrowser
from pathlib import Path

import pyautogui
import pyperclip


class Desktop:

    APPS = {

        "chrome": "chrome",

        "edge": "msedge",

        "firefox": "firefox",

        "whatsapp": "WhatsApp",

        "calculator": "calc",

        "paint": "mspaint",

        "notepad": "notepad",

        "cmd": "cmd",

        "powershell": "powershell",

        "terminal": "wt",

        "task manager": "taskmgr",

        "explorer": "explorer",

        "vs code": "code",

        "vscode": "code",

        "settings": "ms-settings:"

    }

    FOLDERS = {

        "desktop": str(Path.home() / "Desktop"),

        "downloads": str(Path.home() / "Downloads"),

        "documents": str(Path.home() / "Documents"),

        "pictures": str(Path.home() / "Pictures"),

        "videos": str(Path.home() / "Videos"),

        "music": str(Path.home() / "Music")

    }

    # ---------------------------------

    def windows_search(self, text):

        pyautogui.press("win")

        time.sleep(0.6)

        pyperclip.copy(text)

        pyautogui.hotkey("ctrl", "v")

        time.sleep(1)

        pyautogui.press("enter")

    # ---------------------------------

    def open(self, target):

        target = target.strip()

        if target.lower() in self.APPS:

            self.windows_search(

                self.APPS[target.lower()]

            )

            return True

        if target.lower() in self.FOLDERS:

            os.startfile(

                self.FOLDERS[target.lower()]

            )

            return True

        # Unknown application

        self.windows_search(target)

        return True

    # ---------------------------------

    def open_folder(self, folder):

        folder = folder.lower()

        if folder in self.FOLDERS:

            os.startfile(self.FOLDERS[folder])

            return True

        return False

    # ---------------------------------

    def open_file(self, filepath):

        if os.path.exists(filepath):

            os.startfile(filepath)

            return True

        return False

    # ---------------------------------

    def open_url(self, url):

        webbrowser.open(url)

    # ---------------------------------

    def search_windows(self, text):

        self.windows_search(text)

    # ---------------------------------

    def type_text(self, text):

        pyperclip.copy(text)

        pyautogui.hotkey("ctrl", "v")

    # ---------------------------------

    def press_enter(self):

        pyautogui.press("enter")

    # ---------------------------------

    def hotkey(self, *keys):

        pyautogui.hotkey(*keys)

    # ---------------------------------

    def click(self, x, y):

        pyautogui.click(x, y)

    # ---------------------------------

    def write(self, text):

        pyautogui.write(text)

    # ---------------------------------

    def minimize(self):

        pyautogui.hotkey("win", "down")

    # ---------------------------------

    def maximize(self):

        pyautogui.hotkey("win", "up")

    # ---------------------------------

    def close_active(self):

        pyautogui.hotkey("alt", "f4")

    # ---------------------------------

    def screenshot(self, path):

        image = pyautogui.screenshot()

        image.save(path)

        return path


desktop = Desktop()