"""
=========================================
JARVIS SMART BROWSER V2
=========================================
"""

import webbrowser
import urllib.parse


class Browser:

    WEBSITES = {

        "google": "https://www.google.com",

        "youtube": "https://www.youtube.com",

        "github": "https://github.com",

        "chatgpt": "https://chat.openai.com",

        "gmail": "https://mail.google.com",

        "linkedin": "https://www.linkedin.com",

        "instagram": "https://www.instagram.com",

        "facebook": "https://www.facebook.com",

        "twitter": "https://x.com",

        "stackoverflow": "https://stackoverflow.com",

        "amazon": "https://amazon.in",

        "netflix": "https://www.netflix.com",

        "spotify": "https://open.spotify.com"

    }

    # --------------------------------

    def open(self, target):

        target = target.lower().strip()

        if target in self.WEBSITES:

            webbrowser.open(self.WEBSITES[target])

            return True

        return False

    # --------------------------------

    def google(self, query):

        url = (

            "https://www.google.com/search?q=" +

            urllib.parse.quote(query)

        )

        webbrowser.open(url)

    # --------------------------------

    def youtube(self, query):

        url = (

            "https://www.youtube.com/results?search_query=" +

            urllib.parse.quote(query)

        )

        webbrowser.open(url)

    # --------------------------------

    def maps(self, place):

        url = (

            "https://www.google.com/maps/search/" +

            urllib.parse.quote(place)

        )

        webbrowser.open(url)

    # --------------------------------

    def open_url(self, url):

        if not url.startswith("http"):

            url = "https://" + url

        webbrowser.open(url)


browser = Browser()