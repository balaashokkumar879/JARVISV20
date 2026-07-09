"""
=========================================
AI ACTIONS
=========================================
"""

from tools.desktop import desktop
from tools.browser import browser
from tools.whatsapp import whatsapp


class AIActions:

    def execute(self, action: dict):

        intent = action.get("intent")

        if intent == "OPEN_APP":

            return desktop.open(action["app"])

        if intent == "OPEN_WEBSITE":

            return browser.open(action["website"])

        if intent == "GOOGLE":

            browser.google(action["query"])

            return True

        if intent == "YOUTUBE":

            browser.youtube(action["query"])

            return True

        if intent == "WHATSAPP":

            whatsapp.send_message(

                action["contact"],

                action["message"]

            )

            return True

        return False


ai_actions = AIActions()