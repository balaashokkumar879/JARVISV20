"""
=========================================
JARVIS VOICE ENGINE
=========================================
"""

import speech_recognition as sr
import pyttsx3

from config import (
    VOICE_RATE,
    VOICE_VOLUME,
    VOICE_ID
)


class Voice:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        self.microphone = sr.Microphone()

        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", VOICE_RATE)
        self.engine.setProperty("volume", VOICE_VOLUME)

        voices = self.engine.getProperty("voices")

        if voices:

            index = min(VOICE_ID, len(voices) - 1)

            self.engine.setProperty(
                "voice",
                voices[index].id
            )

        with self.microphone as source:

            print("Calibrating microphone...")

            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

    # ----------------------------------

    def speak(self, text: str):

        print(f"Jarvis : {text}")

        self.engine.say(text)

        self.engine.runAndWait()

    # ----------------------------------

    def listen(self):

        try:

            with self.microphone as source:

                print("\nListening...")

                audio = self.recognizer.listen(

                    source,

                    timeout=5,

                    phrase_time_limit=10

                )

            text = self.recognizer.recognize_google(

                audio

            )

            print(f"You : {text}")

            return text

        except sr.WaitTimeoutError:

            return ""

        except sr.UnknownValueError:

            return ""

        except Exception as e:

            print(e)

            return ""

    # ----------------------------------

    def keyboard(self):

        text = input("\nYou : ")

        return text.strip()