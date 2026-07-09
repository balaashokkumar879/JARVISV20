"""
=========================================
BACKGROUND SERVICES
=========================================
"""

from core.observer import observer


class Services:

    def start(self):

        observer.start()

    def stop(self):

        observer.stop()