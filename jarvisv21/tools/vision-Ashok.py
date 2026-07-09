"""
=========================================
JARVIS VISION ENGINE
=========================================
"""

import cv2
import numpy as np
import pytesseract
import pyautogui

from PIL import Image

from config import TESSERACT_PATH


pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


class Vision:

    def __init__(self):
        pass

    # ---------------------------------

    def screenshot(self):

        img = pyautogui.screenshot()

        return img

    # ---------------------------------

    def read_text(self):

        image = self.screenshot()

        text = pytesseract.image_to_string(image)

        return text

    # ---------------------------------

    def locate_text(self, target):

        image = self.screenshot()

        data = pytesseract.image_to_data(

            image,

            output_type=pytesseract.Output.DICT

        )

        target = target.lower()

        n = len(data["text"])

        for i in range(n):

            word = data["text"][i].strip().lower()

            if word == target:

                x = data["left"][i]
                y = data["top"][i]
                w = data["width"][i]
                h = data["height"][i]

                return (

                    x + w // 2,

                    y + h // 2

                )

        return None

    # ---------------------------------

    def click_text(self, text):

        point = self.locate_text(text)

        if point:

            pyautogui.moveTo(

                point[0],

                point[1],

                duration=0.2

            )

            pyautogui.click()

            return True

        return False

    # ---------------------------------

    def exists(self, text):

        return self.locate_text(text) is not None


vision = Vision()